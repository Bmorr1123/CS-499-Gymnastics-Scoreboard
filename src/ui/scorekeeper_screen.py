import sys

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
        self.name1 = QLabel("Gymnast Name")
        self.name1.setFont(QFont('Arial', 15))
        scoreInfo1.addWidget(self.name1)
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
        self.nextGymnast1 = QPushButton("Next Gymnast")
        topButtons1.addWidget(self.nextGymnast1)

        self.orderButton1.clicked.connect(self.activated1)

        self.addLayout(scoreInfo1, 0, 0)
        self.addWidget(self.timer1, 1, 0)
        self.addLayout(outOrder1, 0, 1, 2, 1)
        self.addLayout(topButtons1, 0, 2)

        self.substitution_widget = None

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
        self.nextEvent = QPushButton("Next Event")
        nextButtons.addWidget(self.nextEvent)
        self.finish = QPushButton("Finish Meet")
        nextButtons.addWidget(self.finish)
        self.finish.clicked.connect(self.meetDone)

        for layout in self.quadrants:
            mainLayout.addLayout(layout)
        mainLayout.addLayout(nextButtons)
        self.setLayout(mainLayout)

    def update_Score(self, score, team):
        print(float(score))
        screensController.update_score(team, float(score))

    def meetDone(self):
        screensController.close_windows()
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
