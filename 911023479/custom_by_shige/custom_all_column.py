from aqt import QDialog, QScrollArea, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton, QLabel, QApplication, QWidget


WIDGET_WIDTH = 500
WIDGET_HEIGHT = 430

class ColumnDialog(QDialog):
    def __init__(self, parent=None, deckbrowser=None):
        super().__init__(parent)
        self.deckbrowser = deckbrowser

        self.initUI()

    def initUI(self):
        from ..config import getUserOption
        self.columns = getUserOption("columns")

        layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        self.checkboxes = []
        for column in self.columns:
            if "name" in column and "present" in column:
                # checkbox = QCheckBox(column["name"])

                from ..strings import defaultHeader
                checkbox = QCheckBox(f'{defaultHeader[column["name"]]} | {column["description"]}')

                checkbox.setChecked(column["present"])
                self.checkboxes.append((checkbox, column))
                scroll_layout.addWidget(checkbox)

        # added ---------
        self.preset_option = getUserOption("option")
        self.FSRS_desire_retention = getUserOption("FSRS_desire_retention", True)
        self.maximum_interval = getUserOption("maximum_interval", True)

        self.preset_option_checkbox = QCheckBox("Deck Preset name")
        self.preset_option_checkbox.setChecked(self.preset_option)
        scroll_layout.addWidget(self.preset_option_checkbox)

        self.FSRS_desire_retention_checkbox = QCheckBox("FSRS Desire Retention")
        self.FSRS_desire_retention_checkbox.setChecked(self.FSRS_desire_retention)
        scroll_layout.addWidget(self.FSRS_desire_retention_checkbox)

        self.maximum_interval_checkbox = QCheckBox("Maximum Interval")
        self.maximum_interval_checkbox.setChecked(self.maximum_interval)
        scroll_layout.addWidget(self.maximum_interval_checkbox)
        # ----------------


        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.save_and_close)
        button_layout.addWidget(ok_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)
        button_layout.addWidget(cancel_button)

        button_layout.addStretch()
        layout.addLayout(button_layout)
        self.setLayout(layout)
        self.setWindowTitle("Toggle on or off for all columns")

        self.resize(WIDGET_WIDTH, WIDGET_HEIGHT)

    def save_and_close(self):
        for checkbox, column in self.checkboxes:
            column["present"] = checkbox.isChecked()

        from ..config import getUserOption
        userOption = getUserOption()

        userOption["option"] = self.preset_option_checkbox.isChecked()
        userOption["FSRS_desire_retention"] = self.FSRS_desire_retention_checkbox.isChecked()
        userOption["maximum_interval"] = self.maximum_interval_checkbox.isChecked()

        from ..config import writeConfig
        writeConfig()
        self.deckbrowser.show()
        self.close()


def open_all_column_dialog(self, deckbrowser):
    dialog = ColumnDialog(self, deckbrowser)
    dialog.exec()
