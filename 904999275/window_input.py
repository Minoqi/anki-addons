import anki
import aqt, os, json, base64, re
from aqt.utils import *
from aqt.qt import QObject, QShortcut, QRect, QMainWindow

if qtmajor == 6:
    from PyQt6 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
elif qtmajor == 5:
    from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from .constants import *
from .utils import clip_img_to_md, get_path, get_colors

_config = {}
_dlgs = {}

###########################################################################
class Bridge(QObject):
    """Class to handle js bridge"""
    @pyqtSlot(str, result=str)
    def cmd(self, cmd):
        if cmd == "clipboard_image_to_markdown":
            return json.dumps(clip_img_to_md())

###########################################################################
class IM_window(QMainWindow):
    """Main window to edit markdown in external window"""

    ###########################################################################
    def __init__(self, editor: aqt.editor.Editor, note: anki.notes.Note, fid: int):
        """Constructor: Populates and shows window"""
        global _config, _dlgs
        super().__init__(None, Qt.WindowType.Window)
        _dlgs[hex(id(self))] = self # Save ref to prevent garbage collection

        # Note and field to edit
        self.editor = editor
        self.nid = note.id
        self.fid = fid

        # Create UI
        cwidget = QWidget(self)
        self.setCentralWidget(cwidget)
        vlayout = QVBoxLayout(cwidget)
        vlayout.setContentsMargins(0, 0, 0, 0)

        self.web = QWebEngineView(self)
        self.web.settings().setAttribute(QWebEngineSettings.WebAttribute.FocusOnNavigationEnabled, True)
        self.web.page().setBackgroundColor(theme_manager.qcolor(aqt.colors.CANVAS))
        channel = QWebChannel(self.web)
        py = Bridge(self)
        channel.registerObject("py", py)
        self.web.page().setWebChannel(channel)

        vlayout.addWidget(self.web)
        btns = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok, self)
        vlayout.addWidget(btns)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)
        btns.setContentsMargins(5, 0, 5, 5)
        self.resize(600, 800)
        html = f'''
        <html{' class="night-mode"' if aqt.theme.theme_manager.get_night_mode() else ''}>
        <head>
            <link rel=stylesheet href="_anki/css/webview.css">
            <link rel=stylesheet href="{ADDON_RELURL}/mdi.css">
            <link rel=stylesheet href="{ADDON_RELURL}/{get_path('cm.css')}">
            <script src="{ADDON_RELURL}/window_input.js"></script>
            <script type="text/javascript" src="qrc:///qtwebchannel/qwebchannel.js"></script>
            <script type="text/javascript">
                var pycmd, bridgeCommand
                new QWebChannel(qt.webChannelTransport, function(channel) {{
                    pycmd = bridgeCommand = function (cmd, cb = (() => {{}})) {{
                        channel.objects.py.cmd(cmd, (res) => cb(JSON.parse(res)))
                        return false
                    }}
                }})
            </script>
        </head>
        <body class="{aqt.theme.theme_manager.body_class()} mdi-window">
            <div id="cm-container"></div>
            <script type="text/javascript">
                const mdi_editor = new MarkdownInput.WindowEditor(
                    document.getElementById('cm-container'),
                    {json.dumps(_config)}
                )
                mdi_editor.set_html({json.dumps(note.items())}, {self.fid})
                mdi_editor.editor.cm.focus()
            </script>
        </body>
        </html>
        '''
        self.web.setHtml(html, QUrl(aqt.mw.serverURL()))

        name = note.items()[0][1] or "[new]"
        if len(name) > 15:
            name = name[:15] + "..."

    def __del__(self):
        global _dlgs
        _dlgs.pop(hex(id(self)), None)

    ###########################################################################
    def accept(self) -> None:
        """Main window accept"""
        global _config
        def save_field(res):
            if not res:
                return
            if self.editor.addMode or self.editor.note.id == self.nid:
                note = self.editor.note
                focus = True
            else:
                note = aqt.mw.col.get_note(self.nid)
                focus = False

            if type(res) == str: # Partial note
                note.fields[self.fid] = res
            else: # Complete note
                for (title, content) in res: note[title] = content

            if focus: self.editor.loadNoteKeepingFocus()
            else: aqt.mw.col.update_note(note)

        self.web.page().runJavaScript(f'''(function () {{
            return mdi_editor.get_html();
        }})();''', save_field)
        _config[WINDOW_INPUT][LAST_GEOM] = base64.b64encode(self.saveGeometry()).decode('utf-8')
        aqt.mw.addonManager.writeConfig(__name__, _config)
        super().close()

    ###########################################################################
    def reject(self):
        """Main window reject"""
        global _config
        _config[WINDOW_INPUT][LAST_GEOM] = base64.b64encode(self.saveGeometry()).decode('utf-8')
        aqt.mw.addonManager.writeConfig(__name__, _config)
        super().close()

###########################################################################
def edit_field(editor: aqt.editor.Editor):
    """Open the markdown window for selected field"""
    global _config

    if editor.currentField == None:
        return
    dlg = IM_window(editor, editor.note, editor.currentField)
    if _config[WINDOW_INPUT][SC_ACCEPT]:
        QShortcut(_config[WINDOW_INPUT][SC_ACCEPT], dlg).activated.connect(dlg.accept)
    if _config[WINDOW_INPUT][SC_REJECT]:
        QShortcut(_config[WINDOW_INPUT][SC_REJECT], dlg).activated.connect(dlg.reject)

    if _config[WINDOW_INPUT][SIZE_MODE].lower() == 'last':
        dlg.restoreGeometry(base64.b64decode(_config[WINDOW_INPUT][LAST_GEOM]))
    elif match:= re.match(r'^(\d+)x(\d+)', _config[WINDOW_INPUT][SIZE_MODE]):
        par_geom = editor.parentWindow.geometry()
        geom = QRect(par_geom)
        scr_geom = aqt.mw.app.primaryScreen().geometry()

        geom.setWidth(int(match.group(1)))
        geom.setHeight(int(match.group(2)))
        if geom.width() > scr_geom.width():
            geom.setWidth(scr_geom.width())
        if geom.height() > scr_geom.height():
            geom.setHeight(scr_geom.height())
        geom.moveCenter(par_geom.center())
        if geom.x() < 0:
            geom.setX(0)
        if geom.y() < 0:
            geom.setY(0)

        dlg.setGeometry(geom)
    else:
        dlg.setGeometry(editor.parentWindow.geometry())

    dlg.show()

###########################################################################
def init(cfg: object):
    """Configure and activate markdown input window"""
    global _config
    def editor_btn(buttons, editor):
        btn = editor.addButton(
            os.path.join(ADDON_PATH, "markdown.png"),
            "md_dlg_btn",
            edit_field,
            tip=f"Markdown Input ({_config[WINDOW_INPUT][SC_OPEN]})",
            keys=_config[WINDOW_INPUT][SC_OPEN]
            )
        buttons.append(btn)
        return buttons

    _config = cfg
    aqt.gui_hooks.editor_did_init_buttons.append(editor_btn)

