import pprint
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import arena_screen
import constants
import json_management
import scorekeeper_screen
from db_interface import DBInterface
from data import MeetData
from models import Lineup, LineupEntry


class SchoolSelection(QWidget):
    def __init__(self, school_num, parent):
        super().__init__()
        self.school_num = school_num
        self.db_interface = DBInterface.get_interface()
        self.selected_school: str | None = None
        self.parent: QWidget = parent

        self.setWindowTitle("Schools")

        schools = QVBoxLayout()
        self.selectTitle = QLabel("Select School")
        self.selectTitle.setFont(QFont('Arial', 10))
        self.selectTitle.setAlignment(Qt.AlignCenter)
        schools.addWidget(self.selectTitle)

        self.schoolList = QListWidget()
        # for school in setupController.db_int.get_schools():
        #     QListWidgetItem(school.school_name, self.schoolList)
        for school in self.db_interface.get_schools():
            QListWidgetItem(school.school_name, self.schoolList)

        schools.addWidget(self.schoolList)
        self.schoolList.itemClicked.connect(self.school_clicked)

        self.setLayout(schools)

    def school_clicked(self, clicked_item):
        print("Selected:", clicked_item.text())
        self.selected_school = clicked_item.text()
        MeetData.get_data().schools[self.school_num] = self.selected_school
        self.parent.school1.setText(f"Change from \"{self.selected_school}\"")
        print(MeetData.get_data().schools)
        self.close()

        # school_selected = setupController.db_int.get_school_by_name(clicked_item.text())
        # setupController.schools_selected.append(school_selected[0])


class BlankLineups(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.blankLineups = QVBoxLayout()
        self.blankLabel = QLabel("")
        self.blankLabel.setFont(QFont('Arial', 20))
        self.blankLineups.addWidget(self.blankLabel)
        self.setLayout(self.blankLineups)


class LineupWidget(QWidget):
    def __init__(self, school_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_interface = DBInterface.get_interface()
        self.data = MeetData.get_data()
        self.school_number = school_number

        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)

        self.school1 = QPushButton(f"Select School #{self.school_number + 1}")
        self.school1.clicked.connect(self.show_schools)
        self.insert_lineup_button = QPushButton(f"Insert Lineup {self.school_number + 1} File")
        self.lineup_label = QLabel(f"Lineup {self.school_number + 1}")
        self.lineup_label.setFont(QFont('Arial', 10))
        self.insert_lineup_button.clicked.connect(self.getFile)

        self.vertical_layout.addWidget(self.school1)
        self.vertical_layout.addWidget(self.insert_lineup_button)
        self.vertical_layout.addWidget(self.lineup_label)

        self.school_selector = SchoolSelection(school_number, self)
        self.lineup_objects: None | list[Lineup] = None
        self.lineup_entry_objects: None | list[LineupEntry] = None

    def validate_lineups(self, school_object, lineup_objects, lineup_entry_objects) -> bool:
        # Validating lineup_objects
        valid_app_names = [apparatus_type.short_name for apparatus_type in constants.APPARATUS_TYPES]
        app_names = []
        for lineup_object in lineup_objects:
            if lineup_object.school_id != school_object.school_id:
                self.lineup_label.setText(f"One or more lineups in the file are for the incorrect school!")
                return False
            if lineup_object.apparatus_name not in valid_app_names:
                self.lineup_label.setText(f"Invalid apparatus name \"{lineup_object.apparatus_name}\"!")
                return False
            app_names.append(lineup_object.apparatus_name)

        for i in range(len(app_names)):
            if app_names.count(app_names[i]) > 1:
                self.lineup_label.setText(f"File contains multiple lineups for event \"{app_names[i]}\"!")
                return False

        if len(lineup_objects) != 4:
            self.lineup_label.setText(f"File does not contain 4 lineups!")
            return False

        lineup_entry_counts = {}
        for lineup_entry in lineup_entry_objects:
            if lineup_entry.lineup_id.apparatus_name not in lineup_entry_counts:
                lineup_entry_counts[lineup_entry.lineup_id.apparatus_name] = 0
            lineup_entry_counts[lineup_entry.lineup_id.apparatus_name] += 1

        for lineup_entry_count in lineup_entry_counts:
            if lineup_entry_counts[lineup_entry_count] != 6:
                self.lineup_label.setText(f"Apparatus \"{lineup_entry_count}\" has the incorrect amount of gymnasts!")
                return False

        # Validating lineup_entry_objects
        if len(lineup_entry_objects) != 24:
            self.lineup_label.setText(f"File does not contain 24 lineup entries!")
            return False
        return True

    def getFile(self):
        if not self.data.schools[self.school_number]:
            self.lineup_label.setText(f"You must select a school before loading a lineup!")
            return

        school_name = self.data.schools[self.school_number]
        matching_schools = self.db_interface.get_school_by_name(school_name)
        assert len(matching_schools) == 1, "Duplicate school in DB"

        school_object = matching_schools[0]

        file_name, *_ = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "JSON files (*.json)")
        if file_name:
            self.lineup_label.setText(file_name)
            json_data = json_management.load_json_from_file(file_name)
            lineup_objects, lineup_entry_objects = json_management.convert_json_to_lineups_and_lineup_entries(
                DBInterface.get_interface(),
                json_data
            )
            if self.validate_lineups(school_object, lineup_objects, lineup_entry_objects):
                self.lineup_objects, self.lineup_entry_objects = lineup_objects, lineup_entry_objects

            # json_management.load_lineups_from_file(setupController.db_int, fileName)  UNCOMMENT ME
        else:
            self.lineup_label.setText(f"Lineup {self.school_number}")

    def show_schools(self):
        self.school_selector.show()


class LineupSetupLayout(QStackedLayout):
    def __init__(self, school_number):
        super().__init__()
        self.addWidget(BlankLineups())
        self.lineup_widget = LineupWidget(school_number)
        self.addWidget(self.lineup_widget)
        self.setCurrentIndex(0)

    def has_lineups(self) -> bool:
        # Check if both are filled
        return bool(self.lineup_widget.lineup_objects and self.lineup_widget.lineup_entry_objects)

    def get_lineups_and_entries(self) -> tuple[list[Lineup], list[LineupEntry]]:
        return self.lineup_widget.lineup_objects, self.lineup_widget.lineup_entry_objects


class SetupScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.db_interface = DBInterface.get_interface()
        self.meet_format = 4

        self.setWindowTitle("Setup Screen")

        # create a QGridLayout instance for outer layout
        self.grid_format = QGridLayout()

        # create inner layout instances for widgets
        self.customization_section_layout = QVBoxLayout()  # customization section layout
        self.customization_checkboxes_layout = QVBoxLayout()  # checkboxes layout for customization

        self.meet_format_selection_layout = QVBoxLayout()  # meet format selection layout
        self.meet_format_buttons_layout = QHBoxLayout()  # meet format buttons layout

        self.lineups_insertion_layout = QVBoxLayout()  # team lineups insertion layout
        self.lineups_format_layout = QVBoxLayout()  # layout that holds insertion buttons
        self.lineups = [LineupSetupLayout(i) for i in range(4)]

        self.judgesInsert = QVBoxLayout()  # judges insertion layout

        self.otherButtons = QHBoxLayout()  # "reset selection" and "setup done" button layout

        # add inner layouts to outer layouts
        self.grid_format.addLayout(self.customization_section_layout, 0, 0)
        self.grid_format.addLayout(self.meet_format_selection_layout, 0, 1)
        self.grid_format.addLayout(self.lineups_insertion_layout, 1, 0)
        self.grid_format.addLayout(self.judgesInsert, 1, 1)
        self.grid_format.addLayout(self.otherButtons, 2, 1)

        # create & add necessary widgets/layouts to customization layout
        customizationTitle = QLabel("Customization")
        customizationTitle.setFont(QFont('Arial', 10))
        customizationTitle.setAlignment(Qt.AlignCenter)
        self.customization_section_layout.addWidget(customizationTitle)

        self.logoCheckbox = QCheckBox("Display Logos")
        self.logoCheckbox.setChecked(False)
        self.customization_checkboxes_layout.addWidget(self.logoCheckbox)
        self.orderCheckbox = QCheckBox("Display Order")
        self.orderCheckbox.setChecked(False)
        self.customization_checkboxes_layout.addWidget(self.orderCheckbox)
        self.svCheckbox = QCheckBox("Display Start Value")
        self.svCheckbox.setChecked(False)
        self.customization_checkboxes_layout.addWidget(self.svCheckbox)
        self.judgesCheckbox = QCheckBox("Display Judges")
        self.judgesCheckbox.setChecked(False)
        self.customization_checkboxes_layout.addWidget(self.judgesCheckbox)
        self.customization_section_layout.addLayout(self.customization_checkboxes_layout)

        # create & add necessary widgets/layouts to meet format select layout
        formatTitle = QLabel("Meet Format")
        formatTitle.setFont(QFont('Arial', 10))
        formatTitle.setAlignment(Qt.AlignCenter)
        self.meet_format_selection_layout.addWidget(formatTitle)

        self.meet_type_selection_buttons = []
        for meet_type in constants.MEET_TYPES:
            button = QRadioButton(meet_type.short_name)
            button.setChecked(False)
            button.toggled.connect(
                lambda _, x=meet_type.team_count: self.change_meet_format(x)
            )
            self.meet_type_selection_buttons.append(button)
            self.meet_format_buttons_layout.addWidget(button)

        self.meet_format_selection_layout.addLayout(self.meet_format_buttons_layout)

        # create & add necessary widgets/layouts to lineups insertion layout
        lineupsTitle = QLabel("Team Lineups")
        lineupsTitle.setFont(QFont('Arial', 10))
        lineupsTitle.setAlignment(Qt.AlignCenter)
        self.lineups_insertion_layout.addWidget(lineupsTitle)

        for layout in self.lineups:
            self.lineups_format_layout.addLayout(layout)

        self.lineups_insertion_layout.addLayout(self.lineups_format_layout)

        # create & add necessary widgets to judges insertion layout
        judgesTitle = QLabel("Judges")
        judgesTitle.setFont(QFont('Arial', 10))
        judgesTitle.setAlignment(Qt.AlignCenter)
        self.judgesInsert.addWidget(judgesTitle)

        self.judgeInButton = QPushButton("Insert File of Judges")
        self.judgesLabel = QLabel("List of Judges")
        self.judgesLabel.setFont(QFont('Arial', 10))
        self.judgeInButton.clicked.connect(self.getFile)
        self.judgesInsert.addWidget(self.judgeInButton)
        self.judgesInsert.addWidget(self.judgesLabel)

        # create & add necessary widgets to the other buttons layout
        # self.resetButton = QPushButton("Reset Selections")
        # self.resetButton.clicked.connect(self.reset_selections)
        # self.otherButtons.addWidget(self.resetButton)
        self.doneButton = QPushButton("Finish Setup")
        # NEED TO ADD FUNCTION ONCE SCOREKEEPER IS DONE
        self.doneButton.clicked.connect(self.doneClicked)
        self.otherButtons.addWidget(self.doneButton)

        # set the main layout on the application's window
        self.setLayout(self.grid_format)
        self._arena_screen = None
        self._scorekeeper_screen = None

    def doneClicked(self):
        current_data = MeetData.get_data()
        if not current_data.meet_format:
            print("NEED TO SELECT MEET FORMAT BEFORE PROCEEDING")
            format_msg = QMessageBox()
            format_msg.setIcon(QMessageBox.Critical)
            format_msg.setText("NEED TO SELECT MEET FORMAT BEFORE PROCEEDING")
            format_msg.setWindowTitle("Select Meet Format")
            show_msg = format_msg.exec()
            return

        school_slots_filled = [bool(school) for school in current_data.schools[0:current_data.meet_format]]
        if not all(school_slots_filled):
            print(f"NEED TO SELECT SCHOOLS BEFORE PROCEEDING GOT: {sum(school_slots_filled)} EXPECTED: {current_data.meet_format}.")
            school_msg = QMessageBox()
            school_msg.setIcon(QMessageBox.Critical)
            school_msg.setText(f"NEED TO SELECT SCHOOLS BEFORE PROCEEDING GOT: {sum(school_slots_filled)} EXPECTED: {current_data.meet_format}.")
            school_msg.setWindowTitle("Select Schools")
            show_msg = school_msg.exec()
            return

        for i, school in enumerate(current_data.schools):
            if school is not None and current_data.schools.count(school) > 1:
                print(f"FOUND A DUPLICATE SCHOOL: \"{school}\"")
                duplicate_msg = QMessageBox()
                duplicate_msg.setIcon(QMessageBox.Critical)
                duplicate_msg.setText("FOUND A DUPLICATE SCHOOL")
                duplicate_msg.setWindowTitle("Duplicate School")
                show_msg = duplicate_msg.exec()
                return

        lineups_and_entries: list[tuple[list[Lineup], list[LineupEntry]]] = []
        for i in range(current_data.meet_format):
            if not self.lineups[i].has_lineups():
                print(f"SCHOOL #{i + 1} DOES NOT HAVE A LINEUP.")
                lineup_msg = QMessageBox()
                lineup_msg.setIcon(QMessageBox.Critical)
                lineup_msg.setText(f"SCHOOL #{i + 1} DOES NOT HAVE A LINEUP.")
                lineup_msg.setWindowTitle("No Lineup Selected")
                show_msg = lineup_msg.exec()
                return
            lineups_and_entries.append(self.lineups[i].get_lineups_and_entries())

        for lineups, lineup_entries in lineups_and_entries:
            json_management.insert_missing_lineups(self.db_interface, lineups)
            json_management.insert_missing_lineup_entries(self.db_interface, lineup_entries)

        current_data.display_settings.display_logo = self.logoCheckbox.isChecked()
        current_data.display_settings.display_order = self.orderCheckbox.isChecked()
        current_data.display_settings.display_start_value = self.svCheckbox.isChecked()
        current_data.display_settings.display_judges = self.judgesCheckbox.isChecked()
        print(current_data.display_settings)

        self.close()
        self._arena_screen = arena_screen.ArenaScreen()
        self._arena_screen.show()
        self._scorekeeper_screen = scorekeeper_screen.NewScorekeeperScreen()
        self._scorekeeper_screen.show()

    def reset_selections(self):
        self.logoCheckbox.setChecked(False)
        self.orderCheckbox.setChecked(False)
        self.svCheckbox.setChecked(False)
        self.judgesCheckbox.setChecked(False)

        # for button in self.meet_type_selection_buttons:
        #     button.setChecked(False)

        for lineup in self.lineups:
            lineup.setCurrentIndex(0)

        self.judgesLabel.setText("List of Judges")

    def getFile(self):
        fileName, *_ = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "JSON files (*.json)")
        if fileName:
            self.judgesLabel.setText(fileName)
            json_management.load_judges_from_file(self.db_interface, fileName)
        else:
            self.judgesLabel.setText("List of Judges")

    def change_meet_format(self, team_count):
        self.meet_format = team_count
        MeetData.get_data().meet_format = self.meet_format
        for i, lineup_layout in enumerate(self.lineups):
            lineup_layout.setCurrentIndex(i < team_count)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SetupScreen()
    window.show()
    sys.exit(app.exec_())

