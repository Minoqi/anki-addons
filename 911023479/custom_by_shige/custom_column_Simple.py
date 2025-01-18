from aqt import (QDialog, QFrame, QHBoxLayout, QSizePolicy, QTabWidget,
                QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QColorDialog, QWidget)


class CustomColumnDialog(QDialog):
    def __init__(self, column, parent=None, deck_browser=None ):
        super().__init__(parent)
        self.column = column
        self.deckbrowser = deck_browser
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Enhance main window custom by Shige")
        layout = QVBoxLayout()

        tab_widget = QTabWidget()

        # Tab 1: General
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()

        # Name
        if "name" in self.column:
            tab1_layout.addWidget(QLabel(f'<b>[ Column Name ]</b> {self.column["name"]}'))

        # Present
        if "present" in self.column:
            self.present_checkbox = QCheckBox("Show this column")
            self.present_checkbox.setChecked(self.column["present"])
            tab1_layout.addWidget(self.present_checkbox)
            tab1_layout.addWidget(self.create_separator())  # ----------

        # Header
        if "header" in self.column and "name" in self.column:
            tab1_layout.addWidget(QLabel("<b>[ Header of column ]</b>"))
            tab1_layout.addWidget(QLabel("<b>[ Default header ]</b>"))
            from ..strings import defaultHeader
            tab1_layout.addWidget(QLabel(defaultHeader[self.column["name"]]))
            tab1_layout.addWidget(self.create_separator())  # ----------

            tab1_layout.addWidget(QLabel("<b>[ Custom header ]</b>"))
            header_text = "" if self.column["header"] is None else self.column["header"]
            self.header_edit = QLineEdit(header_text)
            tab1_layout.addWidget(self.header_edit)
            tab1_layout.addWidget(self.create_separator())  # ----------

        tab1_layout.addStretch()
        tab1.setLayout(tab1_layout)
        tab_widget.addTab(tab1, "Option1")

        # -------------------------------

        # Tab 2: Header and Description
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()

        # Description
        if "overlay" in self.column:
            tab2_layout.addWidget(QLabel("<b>[ Tooltip ]</b>"))
            self.overlay_checkbox = QCheckBox("Show tooltip")
            self.overlay_checkbox.setChecked(self.column["overlay"] is None)
            tab2_layout.addWidget(self.overlay_checkbox)

        if "description" in self.column:
            tab2_layout.addWidget(QLabel("Tooltip Description"))
            self.description_edit = QLineEdit(self.column["description"])
            tab2_layout.addWidget(self.description_edit)


        # Color
        if "color" in self.column:
            tab2_layout.addWidget(self.create_separator())  # ----------
            tab2_layout.addWidget(QLabel("<b>[ Color ]</b>"))
            color_text = "No Color Selected" if self.column["color"] is None else self.column["color"]
            self.color_label = QLabel(color_text)
            if self.column["color"] is not None:
                self.color_label.setStyleSheet(f"color: {self.column['color']};")
            tab2_layout.addWidget(self.color_label)

            color_button_layout = QHBoxLayout()
            self.color_button = QPushButton("Choose Color")
            self.color_button.clicked.connect(self.choose_color)
            self.color_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
            color_button_layout.addWidget(self.color_button)

            self.reset_color_button = QPushButton("Delete Color")
            self.reset_color_button.clicked.connect(self.reset_color)
            self.reset_color_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
            color_button_layout.addWidget(self.reset_color_button)

            color_button_layout.addStretch()
            tab2_layout.addLayout(color_button_layout)
            tab2_layout.addWidget(self.create_separator())  # ----------


        tab2_layout.addStretch()
        tab2.setLayout(tab2_layout)
        tab_widget.addTab(tab2, "Option2")

        # -------------------------------

        # Tab 3: Advanced
        tab3 = QWidget()
        tab3_layout = QVBoxLayout()

        # Percent
        if "percent" in self.column:
            tab3_layout.addWidget(QLabel("<b>[ Percent ]</b>"))
            self.percent_checkbox = QCheckBox("Show percent")
            self.percent_checkbox.setChecked(self.column["percent"])
            tab3_layout.addWidget(self.percent_checkbox)

        # Absolute
        if "absolute" in self.column:
            self.absolute_checkbox = QCheckBox("Show absolute numbers")
            self.absolute_checkbox.setChecked(self.column["absolute"])
            tab3_layout.addWidget(self.absolute_checkbox)
            tab3_layout.addWidget(self.create_separator())  # ----------

        # Subdeck
        if "subdeck" in self.column:
            tab3_layout.addWidget(QLabel("<b>[ Subdeck ]</b>"))
            self.subdeck_checkbox = QCheckBox("Include Subdecks in calculations")
            self.subdeck_checkbox.setChecked(self.column["subdeck"])
            tab3_layout.addWidget(self.subdeck_checkbox)

        tab3_layout.addStretch()
        tab3.setLayout(tab3_layout)
        tab_widget.addTab(tab3, "Option3")

        layout.addWidget(tab_widget)

        # -------------------------------

        # Buttons
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.ok_button.setFixedWidth(120)
        self.ok_button.clicked.connect(self.save_and_close)
        button_layout.addWidget(self.ok_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setFixedWidth(120)
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_button)
        button_layout.addStretch()

        layout.addLayout(button_layout)
        self.setLayout(layout)


    # color setting ----
    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.temp_color = color.name()
            self.color_label.setText(color.name())
            self.color_label.setStyleSheet(f"color: {color.name()};")
        else:
            self.temp_color = None
            self.color_label.setText("No Color Selected")
            self.color_label.setStyleSheet("")

    def reset_color(self):
        self.temp_color = None
        self.color_label.setText("No Color Selected")
    # color setting ----


    def create_separator(self):
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("border: 1px solid gray")
        return separator


    def save_and_close(self):
        from ..config import writeConfig
        # if hasattr(self, 'name_edit'):
        #     self.column["name"] = self.name_edit.text()
        if hasattr(self, 'description_edit'):
            self.column["description"] = self.description_edit.text()
        if hasattr(self, 'present_checkbox'):
            self.column["present"] = self.present_checkbox.isChecked()
        if hasattr(self, 'absolute_checkbox'):
            self.column["absolute"] = self.absolute_checkbox.isChecked()
        if hasattr(self, 'percent_checkbox'):
            self.column["percent"] = self.percent_checkbox.isChecked()
        if hasattr(self, 'subdeck_checkbox'):
            self.column["subdeck"] = self.subdeck_checkbox.isChecked()
        if hasattr(self, 'overlay_checkbox'):
            self.column["overlay"] = None if self.overlay_checkbox.isChecked() else False
        if hasattr(self, "header_edit"):
            header_text = self.header_edit.text().strip()
            self.column["header"] = None if header_text == "" else header_text
        if hasattr(self, 'temp_color'):
            self.column["color"] = self.temp_color

        writeConfig()
        self.deckbrowser.show()
        self.accept()


