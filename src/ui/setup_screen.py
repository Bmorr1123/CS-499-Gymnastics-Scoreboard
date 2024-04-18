import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import arena_screen
import constants
import json_management
from db_interface import DBInterface
from data import MeetData


class SchoolSelection(QWidget):
    def __init__(self, school_num):
        super().__init__()
        self.school_num = school_num
        self.db_interface = DBInterface.get_interface()
        self.selected_school: str | None = None

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
    def __init__(self, school_number, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_interface = DBInterface.get_interface()
        self.school_number = school_number
        self.parent = parent

        self.vertical_layout = QVBoxLayout()
        self.setLayout(self.vertical_layout)

        self.school1 = QPushButton(f"Select School {self.school_number + 1}")
        self.school1.clicked.connect(self.show_schools)
        self.insert_lineup_button = QPushButton(f"Insert Lineup {self.school_number + 1} File")
        self.lineup_label = QLabel(f"Lineup {self.school_number + 1}")
        self.lineup_label.setFont(QFont('Arial', 10))
        self.insert_lineup_button.clicked.connect(self.getFile)

        self.vertical_layout.addWidget(self.school1)
        self.vertical_layout.addWidget(self.insert_lineup_button)
        self.vertical_layout.addWidget(self.lineup_label)

        self.school_selector = SchoolSelection(school_number)

    def getFile(self):
        fileName, *_ = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "JSON files (*.json)")
        if fileName:
            self.lineup_label.setText(fileName)
            # json_management.load_lineups_from_file(setupController.db_int, fileName)  UNCOMMENT ME
        else:
            self.lineup_label.setText(f"Lineup {self.school_number}")

    def show_schools(self):
        self.school_selector.show()


class LineupSetupLayout(QStackedLayout):
    def __init__(self, school_number):
        super().__init__()
        self.addWidget(BlankLineups())
        self.addWidget(LineupWidget(school_number, self))
        self.setCurrentIndex(0)


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

        for meet_type in constants.MEET_TYPES:
            button = QRadioButton(meet_type.short_name)
            button.setChecked(False)
            button.toggled.connect(
                lambda _, x=meet_type.team_count: self.change_meet_format(x)
            )
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
        self.resetButton = QPushButton("Reset Selections")
        self.resetButton.clicked.connect(self.resetSelections)
        self.otherButtons.addWidget(self.resetButton)
        self.doneButton = QPushButton("Finish Setup")
        # NEED TO ADD FUNCTION ONCE SCOREKEEPER IS DONE
        self.doneButton.clicked.connect(self.doneClicked)
        self.otherButtons.addWidget(self.doneButton)

        # set the main layout on the application's window
        self.setLayout(self.grid_format)
        self._arena_screen = None


    def doneClicked(self):
        current_data = MeetData.get_data()
        if not current_data.meet_format:
            print("NEED TO SELECT MEET FORMAT BEFORE PROCEEDING")
            return

        school_slots_filled = [bool(school) for school in current_data.schools[0:current_data.meet_format]]
        if not all(school_slots_filled):
            print(f"NEED TO SELECT SCHOOLS BEFORE PROCEEDING Got: {sum(school_slots_filled)} Expected: {current_data.meet_format}.")
            return

        for school in current_data.schools:
            if school is not None and current_data.schools.count(school) > 1:
                print(f"FOUND A DUPLICATE SCHOOL: \"{school}\"")
                return

        current_data.display_settings.display_logo = self.logoCheckbox.isChecked()
        current_data.display_settings.display_order = self.orderCheckbox.isChecked()
        current_data.display_settings.display_start_value = self.svCheckbox.isChecked()
        current_data.display_settings.display_judges = self.judgesCheckbox.isChecked()
        print(current_data.display_settings)

        self.close()
        self._arena_screen = arena_screen.ArenaScreen()
        self._arena_screen.show()



    def resetSelections(self):
        self.logoCheckbox.setChecked(False)
        self.orderCheckbox.setChecked(False)
        self.svCheckbox.setChecked(False)
        self.judgesCheckbox.setChecked(False)

        self.button.setChecked(False)
        self.triButton.setChecked(False)
        self.quadButton.setChecked(False)

        self.lineup1.setCurrentIndex(0)
        self.lineup2.setCurrentIndex(0)
        self.lineup3.setCurrentIndex(0)
        self.lineup4.setCurrentIndex(0)

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

