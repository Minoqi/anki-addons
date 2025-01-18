
import os
import random
from aqt import (QHBoxLayout, QLabel, QPixmap,
                QVBoxLayout,QWidget,QIcon,QMessageBox,Qt)
from os.path import join, dirname


POKEBALL_PATH = "pokeball.png"
POPUP_PNG = r"popup_shige.png"


def get_icon_path(name, format="icon"):
    """ pix,icon """
    addon_path = dirname(__file__)
    icon_path = join(addon_path, name)

    if format == "pix":
        return QPixmap(icon_path)
    else:
        return QIcon(icon_path)


class CustomMessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon(get_icon_path(POKEBALL_PATH)))

        layout = QVBoxLayout()
        self.icon_path = get_icon_path(POPUP_PNG, "pix")
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon_path)
        hbox = QHBoxLayout()

        hbox.addWidget(self.icon_label)
        self.text_label = QLabel()
        self.text_label.setWordWrap(False)
        self.text_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        hbox.addWidget(self.text_label)

        self.hbox2 = QHBoxLayout()
        self.hbox2.addStretch(1)

        self.custom_widget = QWidget()
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(self.hbox2)
        self.custom_widget.setLayout(vbox)
        layout = self.layout() # Get default layout
        layout.addWidget(self.custom_widget, 0, 1) # Add custom widget

    def setText(self, text):
        self.text_label.setText(text)

    def setStandardButtons(self, buttons):
        super().setStandardButtons(buttons)
        self.icon_label.setPixmap(self.icon_path)