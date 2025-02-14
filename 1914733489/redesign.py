# -*- coding: utf-8 -*-
# Copyright: Developer Nick
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

"""


Welcome to a brand new way of using Anki! This add-on redesigns Anki from the ground up and is based on the code from the Night Mode add-on (https://ankiweb.net/shared/info/1496166067). It was helpful in creating this redesign and I am very grateful to its author.

Redesign adds a "View" option in the menu bar with options for switching it on and off and modifying select colors. After enabling the redesign, it changes the colors, animations, buttons, and main screens inside Anki.



Acknowledgements:
    Special thanks to the Night Mode author, Krassowski, and the contributors to that code:
    - b50 (initial compatibility with 2.1),
    - ankitest (compatibility with 1508882486),
    - omega3 (useful bug reports and suggestions)
    - colchizin
    - JulyMorning
    - nathanmalloy
    - rathsky

Patreon Contributors:
    (If you wish to have your name or username displayed here, please let me know.)
    - Basiskarten Jura (https://www.basiskarten.de/)
    - Others who wished to remain anonymous!

Copyright: Developer Nick (nickdeveloper.feedback@gmail.com)
License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html except when stated otherwise.
    """




import traceback

from anki.hooks import addHook, runHook
from aqt import appVersion
from aqt import mw

from PyQt5.QtWidgets import QMessageBox

from .actions_and_settings import *
from .internals import alert
from .config import Config, ConfigValueGetter
from .css_class import inject_css_class
from .icons import Icons
from .menu import get_or_create_menu, Menu
from .stylers import Styler
from .styles import Style, MessageBoxStyle

__addon_name__ = 'Redesign'
__version__ = '1.2'
__anki_version__ = '2.1'




if not appVersion.startswith(__anki_version__):
    print(
        (
            'Unsupported version of Anki. '
            'Redesign requires %s to work properly. '
            'Update to Anki 2.1 or higher to use this add-on.'
        ) % __anki_version__
    )




# Add your color replacement mappings here - old: new, comma separated




class StylingManager:
    def __init__(self, app):
        self.styles = Style.members
        self.stylers = [
            styler(app)
            for styler in Styler.members
        ]
        self.config = ConfigValueGetter(app.config)

    @property
    def active_stylers(self):
        return [
            styler
            for styler in self.stylers
            if styler.name not in self.config.disabled_stylers
        ]

    def replace(self):
        for styler in self.active_stylers:
            styler.replace_attributes()

    def restore(self):
        for styler in self.stylers:
            styler.restore_attributes()




class Redesign:

    menu_layout = [
        EnableNightMode,
        EnableInDialogs,
        StyleScrollBars,
        '-',
        #PrimaryColor,
        BackgroundColor,
        CardColor,
        TextColor,
        ResetColors,
        '-',
        #InvertImage,
        #InvertLatex,
        #TransparentLatex,
        '-',
        #ModeSettings,
        #UserColorMap,
        #DisabledStylers,
        '-',
        About
    ]

    def __init__(self):
        self.profile_loaded = False
        self.config = Config(self, prefix='nm_')
        self.config.init_settings()
        self.icons = Icons(mw)
        self.styles = StylingManager(self)

        view_menu = get_or_create_menu('addon_view_menu', '&View')
        self.menu = Menu(
            self,
            '&Redesign',
            self.menu_layout,
            attach_to=view_menu
        )

        addHook('unloadProfile', self.save)
        # Disabled, uses delay in __init__.py
        # addHook('profileLoaded', self.load)
        addHook('prepareQA', self.night_class_injection)
        addHook('loadNote', self.background_bug_workaround)

    def load(self):
        """
        Load configuration from profile, set states of checkable menu objects
        and turn on redesign if it were enabled on previous session.
        """
        self.config.load()
        self.profile_loaded = True

        self.refresh()
        self.update_menu()

        runHook("night_mode_config_loaded", self.config)


    def update_menu(self):
        self.menu.update_checkboxes(self.config.settings)

    def save(self):
        self.config.save()

    def on(self):
        """Turn on redesign."""
        self.styles.replace()
        runHook("night_mode_state_changed", True)

    def off(self):
        """Turn off redesign."""
        self.styles.restore()
        runHook("night_mode_state_changed", False)

    def refresh(self, reload=False):
        """
        Refresh display by re-enabling redesign or normal mode,
        regenerate customizable css strings.
        """
        state = self.config.state_on.value

        if not self.profile_loaded:
            alert(ERROR_NO_PROFILE)
            return

        try:
            if state:
                if reload:
                    self.off()
                self.on()
            else:
                self.off()
        except Exception:
            alert(ERROR_SWITCH % traceback.format_exc())
            return

        # Reload current screen.
        if mw.state == 'review':
            mw.moveToState('overview')
            mw.moveToState('review')
        if mw.state == 'deckBrowser':
            mw.deckBrowser.refresh()
        if mw.state == 'overview':
            mw.overview.refresh()

        # Redraw toolbar (should be always visible).
        mw.toolbar.draw()
        self.update_menu()
        return True

    def about(self):
        about_box = self.message_box()
        about_box.setText(__addon_name__ + ' ' + __version__ + __doc__)
        about_box.setGeometry(300, 300, 250, 150)
        about_box.setWindowTitle('About \n' + __addon_name__ + ' ' + __version__)

        about_box.exec_()

    def message_box(self):
        box = QMessageBox()
        if self.config.state_on.value:
            box_style = MessageBoxStyle(self)
            box.setStyleSheet(box_style.style)
        return box

    def night_class_injection(self, html, card, context):
        html = inject_css_class(self.config.state_on.value, html)
        return html

    def background_bug_workaround(self, editor):

        if self.config.state_on.value:
            javascript = """
            (function bg_bug_workaround()
            {
                function getTextNodeAtPosition(root, index){
                    // Copyright notice:
                    //
                    //  following function is based on a function created by Pery Mimon:
                    //      https://stackoverflow.com/a/38479462
                    //  and is distributed under CC-BY SA 3.0 license terms:
                    //      https://creativecommons.org/licenses/by-sa/3.0/

                    var lastNode = null;
                    var lastIndex = null

                    var treeWalker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT,function next(elem) {
                        if(index >= elem.textContent.length){
                            lastIndex = index
                            index -= elem.textContent.length;
                            lastNode = elem;
                            return NodeFilter.FILTER_REJECT
                        }
                        return NodeFilter.FILTER_ACCEPT;
                    });
                    var c = treeWalker.nextNode();
                    return {
                        node: c ? c : lastNode,
                        position: c ? index : lastIndex
                    };
                }

                var regex = /<(span|strong) style="background-color: rgb\(255, 255, 255\);">(.*?)<\/(span|strong)>/gm

                function background_workaround_callback(raw_field)
                {
                    function get_rid_of_background(){
                        var field = $(raw_field)
                        var html = field.html()

                        if(html.search(regex) == -1)
                            return

                        var selection = window.getSelection()
                        var range = selection.getRangeAt(0)
                        range.setStart(raw_field, 0)
                        var len = range.toString().length

                        field.html(html.replace(regex, '<$1>$2</$1>'))

                        var range = new Range()
                        var pos = getTextNodeAtPosition(raw_field, len)

                        range.setStart(pos.node, pos.position)

                        selection.removeAllRanges()
                        selection.addRange(range)
                    }
                    return get_rid_of_background
                }

                var field = $('.field')

                field.on('keydown', function(e){
                    var raw_field = this
                    var get_rid_of_background = background_workaround_callback(raw_field)

                    if(e.which === 8 || e.which == 46){
                        window.setTimeout(get_rid_of_background, 0)
                    }
                })

                field.on('paste', function(){
                    var raw_field = this
                    var get_rid_of_background = background_workaround_callback(raw_field)

                    window.setTimeout(get_rid_of_background, 100)
                })

            })()
            """
        else:
            javascript = ''

        editor.web.eval(javascript)


ERROR_NO_PROFILE = """Switching to redesign failed: The profile is not loaded yet.
It could be a bug in Anki, or you may have tried to enable the redesign too quickly after starting Anki."""

ERROR_SWITCH = """Switching to redesign failed: Something went wrong.
This is NOT a problem with Anki, so you can try contacting the add-on author for help.

Please provide following traceback when reporting the issue:
%s
"""
