from aqt import (QColor, QDialog, QFrame, QHBoxLayout, QIntValidator, QResizeEvent, QSizePolicy, QTabWidget,
                QVBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QColorDialog, QWidget, Qt)
from .shige_addons import add_shige_addons_tab
from .endroll.endroll import add_credit_tab
from .changelog_tab import add_changelog_tab
from .shige_pop.popup_config import RATE_THIS_URL
from aqt.utils import openLink
from .open_shige_addons_wiki import WikiQLabel


WIDGET_WIDTH = 500
WIDGET_HEIGHT = 455


class CustomColumnDialog(QDialog):
    def __init__(self, column, parent=None, deck_browser=None ):
        super().__init__(parent)
        self.column = column
        self.deckbrowser = deck_browser
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Enhance main window Custom by Shige")
        layout = QVBoxLayout()

        tab_widget = QTabWidget()

        # Tab 1: General
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()

        # Name
        if "name" in self.column:
            column_name_label = WikiQLabel(f'<b>[ Name of selected column ] {self.column["name"]}</b>',
                "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#name-of-selected-column")
            column_name_label.setStyleSheet("font-size: 18px;")  # フォントサイズを18pxに設定
            layout.addWidget(column_name_label)

        # Present
        if "present" in self.column:
            tab1_layout.addWidget(WikiQLabel("<b>[ Show this column ]</b>",
                "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#show-this-column"))
            self.present_checkbox = QCheckBox("Show this column")
            self.present_checkbox.setChecked(self.column["present"])
            tab1_layout.addWidget(self.present_checkbox)
            tab1_layout.addWidget(self.create_separator())  # ----------

        # Header
        if "header" in self.column and "name" in self.column:
            tab1_layout.addWidget(QLabel("<b>[ Header of column ]</b>"))
            tab1_layout.addWidget(QLabel("<b>[ Default header ]</b>"))
            # from ..strings import defaultHeader
            # tab1_layout.addWidget(QLabel(defaultHeader[self.column["name"]]))

            from ..strings import defaultHeader
            default_header_value_label = QLabel()
            default_header_value_label.setText(defaultHeader[self.column["name"]])
            default_header_value_label.setTextFormat(Qt.TextFormat.PlainText)
            default_header_value_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
            tab1_layout.addWidget(default_header_value_label)


            tab1_layout.addWidget(self.create_separator())  # ----------

            tab1_layout.addWidget(WikiQLabel("<b>[ Custom header ]</b>", 
                "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#header"))
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
            tab2_layout.addWidget(WikiQLabel("<b>[ Tooltip ]</b>",
                "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#tooltip"))
            self.overlay_checkbox = QCheckBox("Show tooltip")
            # self.overlay_checkbox.setChecked(self.column["overlay"] is None or isinstance(self.column["overlay"], str))
            self.overlay_checkbox.setChecked(self.column["overlay"] is not False)
            tab2_layout.addWidget(self.overlay_checkbox)

        if "overlay" in self.column:
            tab2_layout.addWidget(QLabel("Tooltip Description (Custom)"))
            if "description" in self.column:
                default_text = self.column["description"] if isinstance(self.column["description"], str) else ""
            else:
                default_text = ""
            self.overlay_edit = QLineEdit(self.column["overlay"] if isinstance(self.column["overlay"], str) else default_text)
            tab2_layout.addWidget(self.overlay_edit)

        if "description" in self.column:
            tab2_layout.addWidget(QLabel("Tooltip Description (Default)"))
            description_text = self.column["description"] if isinstance(self.column["description"], str) else ""
            self.description_edit = QLineEdit(description_text)
            tab2_layout.addWidget(self.description_edit)

        if "description" in self.column and "overlay" in self.column:
            def toggle_overlay_fields():
                is_checked = self.overlay_checkbox.isChecked()
                self.overlay_edit.setEnabled(is_checked)
                # self.description_edit.setEnabled(is_checked)

            self.overlay_checkbox.stateChanged.connect(toggle_overlay_fields)
            toggle_overlay_fields()


        # Color
        if "color" in self.column:
            tab2_layout.addWidget(self.create_separator())  # ----------
            tab2_layout.addWidget(WikiQLabel("<b>[ Color ]</b>",
                "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#color"))
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
            tab3_layout.addWidget(WikiQLabel("<b>[ Percent ]</b>",
                "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#show-percent"))
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
            tab3_layout.addWidget(WikiQLabel("<b>[ Subdeck ]</b>",
                "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#subdecks"))
            self.subdeck_checkbox = QCheckBox("Include Subdecks in calculations")
            self.subdeck_checkbox.setChecked(self.column["subdeck"])
            tab3_layout.addWidget(self.subdeck_checkbox)

        tab3_layout.addStretch()
        tab3.setLayout(tab3_layout)
        tab_widget.addTab(tab3, "Option3")



        # Tab 3: Advanced
        tab4 = QWidget()
        tab4_layout = QVBoxLayout()

        from .custom_all_column import open_all_column_dialog
        tab4_layout.addWidget(WikiQLabel("<b>[ All columns ]</b>",
            "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#toggle-on-or-off-all-columns"))
        self.open_dialog_button = QPushButton("Toggle on or off for all columns")
        self.open_dialog_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.open_dialog_button.clicked.connect(lambda : open_all_column_dialog(self, self.deckbrowser))

        open_dialog_button_layout = QHBoxLayout()
        open_dialog_button_layout.addWidget(self.open_dialog_button)
        open_dialog_button_layout.addStretch()

        tab4_layout.addLayout(open_dialog_button_layout)

        # tab4_layout.addStretch()
        tab4.setLayout(tab4_layout)
        tab_widget.addTab(tab4, "Global1")


        tab5 = QWidget()
        tab5_layout = QVBoxLayout()
        # tab5_layout.addStretch()
        tab5.setLayout(tab5_layout)
        tab_widget.addTab(tab5, "Global2")

        self.setup_global_option(tab4_layout, tab5_layout)

        add_changelog_tab(self, tab_widget)
        add_credit_tab(self, tab_widget)
        add_shige_addons_tab(self, tab_widget)

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


        # Wiki Button
        self.wiki_button = QPushButton("📖Wiki")
        self.wiki_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.wiki_button.setStyleSheet("QPushButton { padding: 2px; }")
        self.wiki_button.clicked.connect(lambda : openLink("https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html"))
        button_layout.addWidget(self.wiki_button)


        # Wiki Button
        self.report_button = QPushButton("🚨Report")
        self.report_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.report_button.setStyleSheet("QPushButton { padding: 2px; }")
        self.report_button.clicked.connect(lambda : openLink("https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#report"))
        button_layout.addWidget(self.report_button)


        # Rate This Button
        self.ratethis_button = QPushButton("👍️Rate This")
        self.ratethis_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.ratethis_button.setStyleSheet("QPushButton { padding: 2px; }")
        self.ratethis_button.clicked.connect(lambda : openLink(RATE_THIS_URL))
        button_layout.addWidget(self.ratethis_button)

        # Patreon Button
        self.patreon_button = QPushButton("💖Patreon")
        self.patreon_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.patreon_button.setStyleSheet("QPushButton { padding: 2px; }")
        self.patreon_button.clicked.connect(lambda : openLink("https://www.patreon.com/Shigeyuki"))
        button_layout.addWidget(self.patreon_button)







        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.adjust_self_size()


    def setup_global_option(self, tab4_layout: QVBoxLayout, tab5_layout: QVBoxLayout):
        from ..config import getUserOption
        userOption = getUserOption()

        # layout = QVBoxLayout()
        # layout_02 = QVBoxLayout()

        tab4_layout.addWidget(WikiQLabel("<b>[ Hide values, Option ]</b>",
            "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#hide-values-of-parent-decks"))
        self.hide_values_of_parent_decks = userOption.get("hide values of parent decks", False)
        self.hide_values_checkbox = QCheckBox("Hide values of parent decks")
        self.hide_values_checkbox.setChecked(self.hide_values_of_parent_decks)
        tab4_layout.addWidget(self.hide_values_checkbox)

        self.hide_values_when_subdecks_shown = userOption.get("hide values of parent decks when subdecks are shown", False)
        self.hide_values_subdecks_checkbox = QCheckBox("Hide values of parent decks when subdecks are shown")
        self.hide_values_subdecks_checkbox.setChecked(self.hide_values_when_subdecks_shown)
        tab4_layout.addWidget(self.hide_values_subdecks_checkbox)


        # self.option = userOption.get("option", True)
        # self.option_checkbox = QCheckBox("Show name of deck option")
        # self.option_checkbox.setChecked(self.option)
        # tab4_layout.addWidget(self.option_checkbox)


        tab4_layout.addWidget(WikiQLabel("<b>[ Colors ]</b>",
            "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#color-1"))
        self.default_column_color = QColor(userOption.get("default column color", "grey"))
        self.default_column_color_button = QPushButton("default column color")
        self.default_column_color_button.setStyleSheet(f"background-color: {self.default_column_color.name()}")
        self.default_column_color_button.clicked.connect(self.open_default_column_color_dialog)
        # layout.addWidget(self.default_column_color_button)

        # Color Empty Button
        self.color_empty = QColor(userOption.get("color empty", "red"))
        self.color_empty_button = QPushButton("color empty")
        self.color_empty_button.setStyleSheet(f"background-color: {self.color_empty.name()}")
        self.color_empty_button.clicked.connect(self.open_color_empty_dialog)

        # Color Empty Descendant Button
        self.color_empty_descendant = QColor(userOption.get("color empty descendant", "green"))
        self.color_empty_descendant_button = QPushButton("color empty descendant")
        self.color_empty_descendant_button.setStyleSheet(f"background-color: {self.color_empty_descendant.name()}")
        self.color_empty_descendant_button.clicked.connect(self.open_color_empty_descendant_dialog)

        # First Row Layout
        clor_first_row_layout = QHBoxLayout()
        clor_first_row_layout.addWidget(self.default_column_color_button)
        clor_first_row_layout.addWidget(self.color_empty_button)
        clor_first_row_layout.addWidget(self.color_empty_descendant_button)
        clor_first_row_layout.addStretch()
        tab4_layout.addLayout(clor_first_row_layout)

        # Marked Background Color Button
        self.marked_background_color = QColor(userOption.get("marked background color", "powderblue"))
        self.marked_background_color_button = QPushButton("marked background color")
        self.marked_background_color_button.setStyleSheet(f"background-color: {self.marked_background_color.name()}")
        self.marked_background_color_button.clicked.connect(self.open_marked_background_color_dialog)

        # Ended Marked Background Color Button
        self.ended_marked_background_color = QColor(userOption.get("ended marked background color", "yellow"))
        self.ended_marked_background_color_button = QPushButton("ended marked background color")
        self.ended_marked_background_color_button.setStyleSheet(f"background-color: {self.ended_marked_background_color.name()}")
        self.ended_marked_background_color_button.clicked.connect(self.open_ended_marked_background_color_dialog)

        # Second Row Layout
        color_second_row_layout = QHBoxLayout()
        color_second_row_layout.addWidget(self.marked_background_color_button)
        color_second_row_layout.addWidget(self.ended_marked_background_color_button)
        color_second_row_layout.addStretch()
        tab4_layout.addLayout(color_second_row_layout)

        # Color ------
        tab4_layout.addWidget(WikiQLabel("<b>[ Color Zero ]</b>",
            "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#color-zero"))
        self.color_zero = userOption.get("color zero", False)
        color_zero_text = "No Color Selected" if self.color_zero is False else self.color_zero
        self.color_zero_label = QLabel(color_zero_text)
        if self.color_zero is not False:
            self.color_zero_label.setStyleSheet(f"color: {self.color_zero};")
        tab4_layout.addWidget(self.color_zero_label)

        color_button_layout = QHBoxLayout()
        self.color_zero_button = QPushButton("Choose Color")
        self.color_zero_button.clicked.connect(self.color_zero_choose_color)
        self.color_zero_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        color_button_layout.addWidget(self.color_zero_button)

        self.reset_color_zero_button = QPushButton("Delete Color")
        self.reset_color_zero_button.clicked.connect(self.color_zero_reset_color)
        self.reset_color_zero_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        color_button_layout.addWidget(self.reset_color_zero_button)

        color_button_layout.addStretch()
        tab4_layout.addLayout(color_button_layout)
        # Color ------


        tab5_layout.addWidget(WikiQLabel("<b>[ Do color, Dot ]</b>",
            "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#do-color-marked-and-do-color-empty"))

        # Do Color Marked Checkbox
        self.do_color_marked = userOption.get("do color marked", True)
        self.do_color_marked_checkbox = QCheckBox("Do color marked")
        self.do_color_marked_checkbox.setChecked(self.do_color_marked)

        # Do Color Empty Checkbox
        self.do_color_empty = userOption.get("do color empty", True)
        self.do_color_empty_checkbox = QCheckBox("Do color empty")
        self.do_color_empty_checkbox.setChecked(self.do_color_empty)

        # Dot in Numbers Checkbox
        self.dot_in_numbers = userOption.get("dot in numbers", True)
        self.dot_in_numbers_checkbox = QCheckBox("Dot in numbers")
        self.dot_in_numbers_checkbox.setChecked(self.dot_in_numbers)

        # Checkbox Layout
        do_checkbox_layout = QHBoxLayout()
        do_checkbox_layout.addWidget(self.do_color_marked_checkbox)
        do_checkbox_layout.addWidget(self.do_color_empty_checkbox)
        do_checkbox_layout.addWidget(self.dot_in_numbers_checkbox)
        do_checkbox_layout.addStretch()
        tab5_layout.addLayout(do_checkbox_layout)


        # tab5_layout.addWidget(WikiQLabel("<b>[ Cap value ]</b>",
        #     "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#cap-value"))

        h_layout = QHBoxLayout()
        h_layout.addWidget((WikiQLabel("<b>[ Cap value ]</b>",
            "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#end-symbol")))
        self.cap_value = userOption.get("cap value", None)
        self.cap_value_edit = QLineEdit(self.cap_value if self.cap_value is not None else "")
        self.cap_value_edit.setValidator(QIntValidator())  # Only numbers can be input
        h_layout.addWidget(self.cap_value_edit)
        tab5_layout.addLayout(h_layout)

        # -- Symbol -------------

        tab5_layout.addWidget(WikiQLabel("<b>[ Symbols ]</b>",
            "https://shigeyukey.github.io/shige-addons-wiki/enhance-main-window.html#end-symbol"))


        # End Symbol
        self.end_symbol = userOption.get("end symbol", ";")
        self.end_symbol_edit = QLineEdit(self.end_symbol)
        end_symbol_label = QLabel("End Symbol:")
        end_symbol_layout = QHBoxLayout()
        end_symbol_layout.addWidget(end_symbol_label)
        end_symbol_layout.addWidget(self.end_symbol_edit)

        # Book Symbol
        self.book_symbol = userOption.get("book symbol", "{")
        self.book_symbol_edit = QLineEdit(self.book_symbol)
        book_symbol_label = QLabel("Book Symbol:")
        book_symbol_layout = QHBoxLayout()
        book_symbol_layout.addWidget(book_symbol_label)
        book_symbol_layout.addWidget(self.book_symbol_edit)

        # First Row Layout
        symbol_first_row_layout = QHBoxLayout()
        symbol_first_row_layout.addLayout(end_symbol_layout)
        symbol_first_row_layout.addLayout(book_symbol_layout)
        symbol_first_row_layout.addStretch()
        tab5_layout.addLayout(symbol_first_row_layout)

        # Given Up Symbol
        self.given_up_symbol = userOption.get("given up symbol", "/")
        self.given_up_symbol_edit = QLineEdit(self.given_up_symbol)
        given_up_symbol_label = QLabel("Given Up Symbol:")
        given_up_symbol_layout = QHBoxLayout()
        given_up_symbol_layout.addWidget(given_up_symbol_label)
        given_up_symbol_layout.addWidget(self.given_up_symbol_edit)

        # Pause Symbol
        self.pause_symbol = userOption.get("pause symbol", "=")
        self.pause_symbol_edit = QLineEdit(self.pause_symbol)
        pause_symbol_label = QLabel("Pause Symbol:")
        pause_symbol_layout = QHBoxLayout()
        pause_symbol_layout.addWidget(pause_symbol_label)
        pause_symbol_layout.addWidget(self.pause_symbol_edit)

        # Second Row Layout
        symbol_second_row_layout = QHBoxLayout()
        symbol_second_row_layout.addLayout(given_up_symbol_layout)
        symbol_second_row_layout.addLayout(pause_symbol_layout)
        symbol_second_row_layout.addStretch()
        tab5_layout.addLayout(symbol_second_row_layout)
        # ---------------


        tab4_layout.addStretch()
        # tab4_layout.addLayout(layout)
        tab5_layout.addStretch()
        # tab5_layout.addLayout(layout_02)

    # color setting ----
    def color_zero_choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_zero = color.name()
            self.color_zero_label.setText(color.name())
            self.color_zero_label.setStyleSheet(f"color: {color.name()};")
        else:
            self.color_zero = False
            self.color_zero_label.setText("No Color Selected")
            self.color_zero_label.setStyleSheet("")

    def color_zero_reset_color(self):
        self.color_zero = False
        self.color_zero_label.setText("No Color Selected")
        self.color_zero_label.setStyleSheet("")
    # color setting ----

    # color setting ----


    def open_default_column_color_dialog(self):
        color = QColorDialog.getColor(self.default_column_color, self)
        if color.isValid():
            self.default_column_color = color
            self.default_column_color_button.setStyleSheet(f"background-color: {self.default_column_color.name()}")

    def open_color_empty_dialog(self):
        color = QColorDialog.getColor(self.color_empty, self)
        if color.isValid():
            self.color_empty = color
            self.color_empty_button.setStyleSheet(f"background-color: {self.color_empty.name()}")

    def open_color_empty_descendant_dialog(self):
        color = QColorDialog.getColor(self.color_empty_descendant, self)
        if color.isValid():
            self.color_empty_descendant = color
            self.color_empty_descendant_button.setStyleSheet(f"background-color: {self.color_empty_descendant.name()}")

    def open_marked_background_color_dialog(self):
        color = QColorDialog.getColor(self.marked_background_color, self)
        if color.isValid():
            self.marked_background_color = color
            self.marked_background_color_button.setStyleSheet(f"background-color: {self.marked_background_color.name()}")

    def open_ended_marked_background_color_dialog(self):
        color = QColorDialog.getColor(self.ended_marked_background_color, self)
        if color.isValid():
            self.ended_marked_background_color = color
            self.ended_marked_background_color_button.setStyleSheet(f"background-color: {self.ended_marked_background_color.name()}")
    # color setting ----


    def save_all_options(self):
        from ..config import writeConfig, getUserOption

        userOption = getUserOption()

        userOption["hide values of parent decks"] = self.hide_values_checkbox.isChecked()
        userOption["hide values of parent decks when subdecks are shown"] = self.hide_values_subdecks_checkbox.isChecked()
        userOption["default column color"] = self.default_column_color.name()
        # userOption["option"] = self.option_checkbox.isChecked()

        text_value = self.cap_value_edit.text().strip()
        if text_value in ["", "0"]:
            userOption["cap value"] = None
        else:
            userOption["cap value"] = int(text_value)
        # userOption["cap value"] = self.cap_value_edit.text()

        userOption["color empty"] = self.color_empty.name()
        userOption["color empty descendant"] = self.color_empty_descendant.name()
        userOption["marked background color"] = self.marked_background_color.name()
        userOption["ended marked background color"] = self.ended_marked_background_color.name()
        userOption["end symbol"] = self.end_symbol_edit.text()
        userOption["book symbol"] = self.book_symbol_edit.text()
        userOption["given up symbol"] = self.given_up_symbol_edit.text()
        userOption["pause symbol"] = self.pause_symbol_edit.text()
        userOption["do color marked"] = self.do_color_marked_checkbox.isChecked()
        userOption["do color empty"] = self.do_color_empty_checkbox.isChecked()
        userOption["dot in numbers"] = self.dot_in_numbers_checkbox.isChecked()
        userOption["color zero"] = self.color_zero

        writeConfig()

    def adjust_self_size(self):
        # min_size = self.layout().minimumSize()
        # self.resize(min_size.width(), min_size.height())
        self.resize(WIDGET_WIDTH, WIDGET_HEIGHT)

    def resizeEvent(self, event:"QResizeEvent"):
        size = event.size()
        print(f"Width: {size.width()}, Height: {size.height()}")
        super().resizeEvent(event)

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
        self.color_label.setStyleSheet("")
    # color setting ----


    def create_separator(self):
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("border: 1px solid gray")
        return separator


    def save_and_close(self):

        # ---- now column option ----------
        from ..config import writeConfig
        # if hasattr(self, 'name_edit'):
        #     self.column["name"] = self.name_edit.text()
        if hasattr(self, 'description_edit'):
            self.column["description"] = self.description_edit.text()

        if hasattr(self, 'overlay_checkbox'):
            if self.overlay_checkbox.isChecked():
                self.column["overlay"] = self.overlay_edit.text() if self.overlay_edit.text() != "" else None
            else:
                self.column["overlay"] = False


        if hasattr(self, 'present_checkbox'):
            self.column["present"] = self.present_checkbox.isChecked()
        if hasattr(self, 'absolute_checkbox'):
            self.column["absolute"] = self.absolute_checkbox.isChecked()
        if hasattr(self, 'percent_checkbox'):
            self.column["percent"] = self.percent_checkbox.isChecked()
        if hasattr(self, 'subdeck_checkbox'):
            self.column["subdeck"] = self.subdeck_checkbox.isChecked()

        if hasattr(self, "header_edit"):
            header_text = self.header_edit.text().strip()
            self.column["header"] = None if header_text == "" else header_text
        if hasattr(self, 'temp_color'):
            self.column["color"] = self.temp_color
        # ---- now column option -------------

        # ---- global column option ----------
        self.save_all_options()

        writeConfig()
        self.deckbrowser.show()
        self.accept()


    # def save_and_close(self):

    #     # ---- now column option ----------
    #     from ..config import writeConfig
    #     # if hasattr(self, 'name_edit'):
    #     #     self.column["name"] = self.name_edit.text()
    #     if hasattr(self, 'description_edit'):
    #         self.column["description"] = self.description_edit.text()
    #     if hasattr(self, 'present_checkbox'):
    #         self.column["present"] = self.present_checkbox.isChecked()
    #     if hasattr(self, 'absolute_checkbox'):
    #         self.column["absolute"] = self.absolute_checkbox.isChecked()
    #     if hasattr(self, 'percent_checkbox'):
    #         self.column["percent"] = self.percent_checkbox.isChecked()
    #     if hasattr(self, 'subdeck_checkbox'):
    #         self.column["subdeck"] = self.subdeck_checkbox.isChecked()
    #     if hasattr(self, 'overlay_checkbox'):
    #         self.column["overlay"] = None if self.overlay_checkbox.isChecked() else False
    #     if hasattr(self, "header_edit"):
    #         header_text = self.header_edit.text().strip()
    #         self.column["header"] = None if header_text == "" else header_text
    #     if hasattr(self, 'temp_color'):
    #         self.column["color"] = self.temp_color
    #     # ---- now column option -------------

    #     # ---- global column option ----------


    #     self.save_all_options()



    #     writeConfig()
    #     self.deckbrowser.show()
    #     self.accept()