from aqt import QWidget, QVBoxLayout, QTabWidget, QTextBrowser
from .shige_pop.popup_config import NEW_FEATURE, OLD_CHANGE_LOG

def add_changelog_tab(self, tab_widget:"QTabWidget"):

    tab4 = QWidget(self)

    log_text = "\n" + NEW_FEATURE + "\n" + OLD_CHANGE_LOG


    change_log = QTextBrowser()
    change_log.setPlainText(log_text)

    tab4_layout = QVBoxLayout()
    tab4_layout.addWidget(change_log)

    tab4_layout = QVBoxLayout()
    tab4_layout.addWidget(change_log)
    tab4.setLayout(tab4_layout)
    tab_widget.addTab(tab4, "log")

