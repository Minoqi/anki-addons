
from aqt import QLabel, Qt
from aqt.utils import openLink
from os.path import join, dirname

addon_path = dirname(__file__)
question_mark = join(addon_path, "question_mark.png")
QUESTION_MARK = f'<img src="{question_mark}" alt="❔️" height="15"></a>'

class WikiQLabel(QLabel):
    def __init__(self, text, url, parent=None):
        super().__init__(parent)
        self.url = url

        if isinstance(text, QLabel):
            text = text.text()

        self.setText(f'{text} <a href="{url}" style="text-decoration:none; vertical-align: middle;">{QUESTION_MARK}</a>')
        self.setOpenExternalLinks(True)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.linkActivated.connect(self.open_link)

        self.setAlignment(Qt.AlignmentFlag.AlignVCenter)

    def open_link(self, link):
        openLink(link)