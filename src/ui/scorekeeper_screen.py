import sys

import constants
import screensController
import postController
import updateController

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from data import MeetData, EventLineupManager
from db_interface import DBInterface
from db.models import Gymnast, Event, Lineup, LineupEntry


class SubstitutionWidget(QWidget):
    def __init__(self, team_num: int):
        super().__init__()
        self.setWindowTitle("Lineup Substitution")

        # create a QVBoxLayout instance
        substitution = QVBoxLayout()

        # create inner layouts for substitutions
        selectLineups = QVBoxLayout()
        subLineups = QGridLayout()

        # create substitution title for window
        subTitle = QLabel("Lineup Substitution")
        subTitle.setFont(QFont('Arial', 30))
        subTitle.setAlignment(Qt.AlignCenter)

        # create selection titles
        selectGymnasts = QLabel("Select Gymnast To Substitute:")
        selectGymnasts.setFont(QFont('Arial', 20))
        selectSubstitution = QLabel("Select Substitution:")
        selectSubstitution.setFont(QFont('Arial', 20))

        # create blank widgets
        blank1 = QListWidget()
        blank2 = QListWidget()

        # create available gymnasts
        # ~team 1~
        self.available_list = QListWidget()
        QListWidgetItem("Gymnast A1", self.available_list)
        QListWidgetItem("Gymnast B1", self.available_list)
        QListWidgetItem("Gymnast C1", self.available_list)
        QListWidgetItem("Gymnast D1", self.available_list)
        QListWidgetItem("Gymnast E1", self.available_list)
        self.available_list.setFont(QFont('Arial', 15))
        available_layout = QVBoxLayout()
        available_layout.addWidget(self.available_list)

        # add available gymnasts for each team to stacked layout
        # self.teamLineup.addWidget(blank1)
        # self.teamLineup.setCurrentIndex(0)

        # create team rosters
        # ~team 1~
        self.roster_list = QListWidget()
        QListWidgetItem("Available A1", self.roster_list)
        QListWidgetItem("Available B1", self.roster_list)
        QListWidgetItem("Available C1", self.roster_list)
        QListWidgetItem("Available D1", self.roster_list)
        QListWidgetItem("Available E1", self.roster_list)
        self.roster_list.setFont(QFont('Arial', 15))
        roster_layout = QVBoxLayout()
        roster_layout.addWidget(self.roster_list)

        # add team rosters for each team to stacked layout
        # self.teamRoster.addWidget(blank2)
        # self.teamRoster.addWidget(self.roster_list)
        # self.teamRoster.setCurrentIndex(0)

        # add substitution mechanic to inner layout
        subLineups.addWidget(selectGymnasts, 0, 0)
        subLineups.addWidget(selectSubstitution, 0, 1)
        subLineups.addLayout(available_layout, 1, 0)
        subLineups.addLayout(roster_layout, 1, 1)

        # add title to main layout
        substitution.addWidget(subTitle)

        # add inner layouts to main layout
        substitution.addLayout(selectLineups)
        substitution.addLayout(subLineups)

        # create and add verify button to bottom of screen
        self.verifyButton = QPushButton("Update Lineup")
        self.verifyButton.setFont(QFont('Arial', 15))
        substitution.addWidget(self.verifyButton)
        self.verifyButton.clicked.connect(self.updateClicked)

        # put function to dropdown menu of team lineups
        # lineupMenu.activated.connect(self.activated)

        # set the layout on the application's window
        self.setLayout(substitution)

    def activated(self, index):
        self.teamLineup.setCurrentIndex(index)
        self.teamRoster.setCurrentIndex(index)

    def updateClicked(self):
        self.close()


class ScorekeeperQuadrant(QGridLayout):
    def __init__(self, team_num: int):
        super().__init__()
        self.db_interface = DBInterface.get_interface()
        self.data = MeetData.get_data()
        self.team_num = team_num

        self.event_lineup_manager: EventLineupManager = self.data.event_lineup_managers[self.team_num]
        # for lineup in self.event_lineup_manager.lineup_objects:
        #     print(lineup)
        # for lineup_entry in self.event_lineup_manager.lineup_entry_objects:
        #     print(lineup_entry)

        scoreInfo1 = QVBoxLayout()
        self.schoolName1 = QLabel(self.data.schools[self.team_num])
        self.schoolName1.setFont(QFont('Arial', 12))
        scoreInfo1.addWidget(self.schoolName1)
        self.current_gymnast_name_label = QLabel("Gymnast Name")
        self.current_gymnast_name_label.setFont(QFont('Arial', 15))
        scoreInfo1.addWidget(self.current_gymnast_name_label)
        self.enterScore1 = QLineEdit()
        self.enterScore1.setFixedWidth(300)
        self.enterScore1.setValidator(QDoubleValidator())
        self.enterScore1.setMaxLength(6)
        self.enterScore1.setAlignment(Qt.AlignLeft)
        self.enterScore1.setFont(QFont('Arial', 15))
        self.enterScore1.returnPressed.connect(lambda: self.update_Score(self.enterScore1.text(), 1))
        # self.enterScore1.returnPressed.connect(lambda: self.enterPressed())
        scoreForm1 = QFormLayout()
        scoreForm1.addRow("Enter Score", self.enterScore1)
        scoreInfo1.addLayout(scoreForm1)

        # create timer labels for each team
        self.timer1 = QLabel("--:--")
        self.timer1.setFont(QFont('Arial', 30))
        self.timer1.setAlignment(Qt.AlignCenter)

        outOrder1 = QVBoxLayout()
        self.orderButton1 = QPushButton("Out of Order")
        self.orderButton1.setCheckable(True)
        self.orderButton1.toggle()
        outOrder1.addWidget(self.orderButton1)
        self.orderSelect1 = QStackedLayout()
        self.blank1 = QListWidget()
        self.selection1 = QComboBox()
        self.selection1.addItems(["Select Next Gymnast...", "Gymnast #1", "Gymnast #2", "Gymnast #3", "Gymnast #4",
                                  "Gymnast #5", "Gymnast #6"])
        self.selection1.setFont(QFont('Arial', 10))
        self.orderSelect1.addWidget(self.blank1)
        self.orderSelect1.addWidget(self.selection1)
        self.orderSelect1.setCurrentIndex(0)
        outOrder1.addLayout(self.orderSelect1)

        topButtons1 = QHBoxLayout()
        self.update1 = QPushButton("Update Lineup")
        topButtons1.addWidget(self.update1)
        self.update1.clicked.connect(self.lineupChange)
        self.next_gymnast_button = QPushButton("Next Gymnast")
        topButtons1.addWidget(self.next_gymnast_button)
        self.next_gymnast_button.clicked.connect(self.next_gymnast)

        self.orderButton1.clicked.connect(self.activated1)

        self.addLayout(scoreInfo1, 0, 0)
        self.addWidget(self.timer1, 1, 0)
        self.addLayout(outOrder1, 0, 1, 2, 1)
        self.addLayout(topButtons1, 0, 2)

        self.substitution_widget = None

    def refresh_ui(self):
        gymnast_id: int | None = self.event_lineup_manager.get_current_gymnast_id()
        if gymnast_id is not None:
            gymnast: Gymnast = self.db_interface.get_gymnast_by_id(gymnast_id)[0]
            self.current_gymnast_name_label.setText(f"{gymnast.first_name} {gymnast.last_name}")
        else:
            self.current_gymnast_name_label.setText("No Gymnast currently.")

    def next_gymnast(self):
        if self.event_lineup_manager.next_gymnast():
            print("Successful transition to next Gymnast")
            self.refresh_ui()
        else:
            print("Failed to go to next Gymnast")

    def lineupChange(self):
        self.substitution_widget = SubstitutionWidget(self.team_num)
        self.substitution_widget.show()

    def activated1(self):
        self.orderSelect1.setCurrentIndex(1)


class NewScorekeeperScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scorekeeper Screen")
        self.data = MeetData.get_data()
        mainLayout = QVBoxLayout()

        self.quadrants = [ScorekeeperQuadrant(i) for i in range(self.data.meet_format)]
        # create 'next event' and 'finish meet' buttons
        nextButtons = QHBoxLayout()
        self.nextEvent = QPushButton("Start Event")
        nextButtons.addWidget(self.nextEvent)
        self.nextEvent.clicked.connect(self.next_event)

        self.finish = QPushButton("Finish Meet")
        nextButtons.addWidget(self.finish)
        self.finish.clicked.connect(self.meetDone)

        for layout in self.quadrants:
            mainLayout.addLayout(layout)
        mainLayout.addLayout(nextButtons)
        self.setLayout(mainLayout)
        self.is_started = False

    def start_event(self):
        apparatus_orders: dict[int, list] = constants.APPARATUS_ORDERING[self.data.meet_format]
        for i, quadrant in enumerate(self.quadrants):
            quadrant.event_lineup_manager.start_event(apparatus_orders[i])

        self.is_started = True

    def next_event(self):
        if not self.is_started:
            self.start_event()
        else:
            for quadrant in self.quadrants:
                quadrant.event_lineup_manager.next_apparatus()

        next_apps = ", ".join([quadrant.event_lineup_manager.get_next_apparatus_name() for quadrant in self.quadrants])
        self.nextEvent.setText(f"Next Event ({next_apps})")

        for quadrant in self.quadrants:
            quadrant.refresh_ui()

    def update_Score(self, score, team):
        print(float(score))
        # screensController.update_score(team, float(score))

    def meetDone(self):
        # screensController.close_windows()
        postController.open_window()


if __name__ == "__main__":
    db_interface = DBInterface.get_interface("../../db_setup/.env")

    meet_data = MeetData.get_data()
    meet_data.meet_format = 4
    meet_data.schools[0] = "University of Kentucky"
    meet_data.schools[1] = "The University of Alabama"
    meet_data.schools[2] = "Louisiana State University"
    meet_data.schools[3] = "University of Missouri"
    app = QApplication(sys.argv)
    scorekeeper = NewScorekeeperScreen()
    scorekeeper.show()
    sys.exit(app.exec_())
