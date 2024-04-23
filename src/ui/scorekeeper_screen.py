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
#
# class ScorekeeperScreen(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Scorekeeper Screen")
#
#         # create a QVBoxLayout instance for the outer layout
#         mainLayout = QVBoxLayout()
#         self.data = MeetData.get_data()
#
#         # create area for score entering for each team
#         scoreInfo1 = QVBoxLayout()
#         self.schoolName1 = QLabel(self.data.schools[0].school_name)
#         self.schoolName1.setFont(QFont('Arial', 12))
#         scoreInfo1.addWidget(self.schoolName1)
#         self.name1 = QLabel("Gymnast Name")
#         self.name1.setFont(QFont('Arial', 15))
#         scoreInfo1.addWidget(self.name1)
#         self.enterScore1 = QLineEdit()
#         self.enterScore1.setFixedWidth(300)
#         self.enterScore1.setValidator(QDoubleValidator())
#         self.enterScore1.setMaxLength(6)
#         self.enterScore1.setAlignment(Qt.AlignLeft)
#         self.enterScore1.setFont(QFont('Arial', 15))
#         self.enterScore1.returnPressed.connect(lambda: self.update_Score(self.enterScore1.text(), 1))
#         # self.enterScore1.returnPressed.connect(lambda: self.enterPressed())
#         scoreForm1 = QFormLayout()
#         scoreForm1.addRow("Enter Score", self.enterScore1)
#         scoreInfo1.addLayout(scoreForm1)
#
#         scoreInfo2 = QVBoxLayout()
#         self.schoolName2 = QLabel(screensController.competingSchools[1].school_name)
#         self.schoolName2.setFont(QFont('Arial', 12))
#         scoreInfo2.addWidget(self.schoolName2)
#         self.name2 = QLabel("Gymnast Name")
#         self.name2.setFont(QFont('Arial', 15))
#         scoreInfo2.addWidget(self.name2)
#         self.enterScore2 = QLineEdit()
#         self.enterScore2.setFixedWidth(300)
#         self.enterScore2.setValidator(QDoubleValidator())
#         self.enterScore2.setMaxLength(6)
#         self.enterScore2.setAlignment(Qt.AlignLeft)
#         self.enterScore2.setFont(QFont('Arial', 15))
#         self.enterScore2.returnPressed.connect(lambda: self.update_Score(self.enterScore2.text(), 2))
#         # self.enterScore2.returnPressed.connect(lambda: self.enterPressed())
#         scoreForm2 = QFormLayout()
#         scoreForm2.addRow("Enter Score", self.enterScore2)
#         scoreInfo2.addLayout(scoreForm2)
#
#         scoreInfo3 = QVBoxLayout()
#         self.schoolName3 = QLabel(screensController.competingSchools[2].school_name)
#         self.schoolName3.setFont(QFont('Arial', 12))
#         scoreInfo3.addWidget(self.schoolName3)
#         self.name3 = QLabel("Gymnast Name")
#         self.name3.setFont(QFont('Arial', 15))
#         scoreInfo3.addWidget(self.name3)
#         self.enterScore3 = QLineEdit()
#         self.enterScore3.setFixedWidth(300)
#         self.enterScore3.setValidator(QDoubleValidator())
#         self.enterScore3.setMaxLength(6)
#         self.enterScore3.setAlignment(Qt.AlignLeft)
#         self.enterScore3.setFont(QFont('Arial', 15))
#         self.enterScore3.returnPressed.connect(lambda: self.update_Score(self.enterScore3.text(), 3))
#         # self.enterScore3.returnPressed.connect(lambda: self.enterPressed())
#         scoreForm3 = QFormLayout()
#         scoreForm3.addRow("Enter Score", self.enterScore3)
#         scoreInfo3.addLayout(scoreForm3)
#
#         scoreInfo4 = QVBoxLayout()
#         self.schoolName4 = QLabel(screensController.competingSchools[3].school_name)
#         self.schoolName4.setFont(QFont('Arial', 12))
#         scoreInfo4.addWidget(self.schoolName4)
#         self.name4 = QLabel("Gymnast Name")
#         self.name4.setFont(QFont('Arial', 15))
#         scoreInfo4.addWidget(self.name4)
#         self.enterScore4 = QLineEdit()
#         self.enterScore4.setFixedWidth(300)
#         self.enterScore4.setValidator(QDoubleValidator())
#         self.enterScore4.setMaxLength(6)
#         self.enterScore4.setAlignment(Qt.AlignLeft)
#         self.enterScore4.setFont(QFont('Arial', 15))
#         self.enterScore4.returnPressed.connect(lambda: self.update_Score(self.enterScore4.text(), 4))
#         # self.enterScore4.returnPressed.connect(lambda: self.enterPressed())
#         scoreForm4 = QFormLayout()
#         scoreForm4.addRow("Enter Score", self.enterScore4)
#         scoreInfo4.addLayout(scoreForm4)
#
#         # create timer labels for each team
#         self.timer1 = QLabel("--:--")
#         self.timer1.setFont(QFont('Arial', 30))
#         self.timer1.setAlignment(Qt.AlignCenter)
#         self.timer2 = QLabel("--:--")
#         self.timer2.setFont(QFont('Arial', 30))
#         self.timer2.setAlignment(Qt.AlignCenter)
#         self.timer3 = QLabel("--:--")
#         self.timer3.setFont(QFont('Arial', 30))
#         self.timer3.setAlignment(Qt.AlignCenter)
#         self.timer4 = QLabel("--:--")
#         self.timer4.setFont(QFont('Arial', 30))
#         self.timer4.setAlignment(Qt.AlignCenter)
#
#         # create area for out of order selection for each team
#         outOrder1 = QVBoxLayout()
#         self.orderButton1 = QPushButton("Out of Order")
#         self.orderButton1.setCheckable(True)
#         self.orderButton1.toggle()
#         outOrder1.addWidget(self.orderButton1)
#         self.orderSelect1 = QStackedLayout()
#         self.blank1 = QListWidget()
#         self.selection1 = QComboBox()
#         self.selection1.addItems(["Select Next Gymnast...", "Gymnast #1", "Gymnast #2", "Gymnast #3", "Gymnast #4",
#                                   "Gymnast #5", "Gymnast #6"])
#         self.selection1.setFont(QFont('Arial', 10))
#         self.orderSelect1.addWidget(self.blank1)
#         self.orderSelect1.addWidget(self.selection1)
#         self.orderSelect1.setCurrentIndex(0)
#         outOrder1.addLayout(self.orderSelect1)
#
#         outOrder2 = QVBoxLayout()
#         self.orderButton2 = QPushButton("Out of Order")
#         self.orderButton2.setCheckable(True)
#         self.orderButton2.toggle()
#         outOrder2.addWidget(self.orderButton2)
#         self.orderSelect2 = QStackedLayout()
#         self.blank2 = QListWidget()
#         self.selection2 = QComboBox()
#         self.selection2.addItems(["Select Next Gymnast...", "Gymnast #1", "Gymnast #2", "Gymnast #3", "Gymnast #4",
#                                   "Gymnast #5", "Gymnast #6"])
#         self.selection2.setFont(QFont('Arial', 10))
#         self.orderSelect2.addWidget(self.blank2)
#         self.orderSelect2.addWidget(self.selection2)
#         self.orderSelect2.setCurrentIndex(0)
#         outOrder2.addLayout(self.orderSelect2)
#
#         if screensController.meetFormat == "Quad" or screensController.meetFormat == "Tri":
#             outOrder3 = QVBoxLayout()
#             self.orderButton3 = QPushButton("Out of Order")
#             self.orderButton3.setCheckable(True)
#             self.orderButton3.toggle()
#             outOrder3.addWidget(self.orderButton3)
#             self.orderSelect3 = QStackedLayout()
#             self.blank3 = QListWidget()
#             self.selection3 = QComboBox()
#             self.selection3.addItems(["Select Next Gymnast...", "Gymnast #1", "Gymnast #2", "Gymnast #3", "Gymnast #4",
#                                       "Gymnast #5", "Gymnast #6"])
#             self.selection3.setFont(QFont('Arial', 10))
#             self.orderSelect3.addWidget(self.blank3)
#             self.orderSelect3.addWidget(self.selection3)
#             self.orderSelect3.setCurrentIndex(0)
#             self.orderButton3.clicked.connect(self.activated3)
#             outOrder3.addLayout(self.orderSelect3)
#
#         if screensController.meetFormat == "Quad":
#             outOrder4 = QVBoxLayout()
#             self.orderButton4 = QPushButton("Out of Order")
#             self.orderButton4.setCheckable(True)
#             self.orderButton4.toggle()
#             outOrder4.addWidget(self.orderButton4)
#             self.orderSelect4 = QStackedLayout()
#             self.blank4 = QListWidget()
#             self.selection4 = QComboBox()
#             self.selection4.addItems(["Select Next Gymnast...", "Gymnast #1", "Gymnast #2", "Gymnast #3", "Gymnast #4",
#                                       "Gymnast #5", "Gymnast #6"])
#             self.selection4.setFont(QFont('Arial', 10))
#             self.orderSelect4.addWidget(self.blank4)
#             self.orderSelect4.addWidget(self.selection4)
#             self.orderSelect4.setCurrentIndex(0)
#             self.orderButton4.clicked.connect(self.activated4)
#             outOrder4.addLayout(self.orderSelect4)
#
#         # put function to 'out of order' buttons
#         self.orderButton1.clicked.connect(self.activated1)
#         self.orderButton2.clicked.connect(self.activated2)
#
#         # create area for 'update lineup' and 'next gymnast' buttons for each team
#         topButtons1 = QHBoxLayout()
#         self.update1 = QPushButton("Update Lineup")
#         topButtons1.addWidget(self.update1)
#         self.update1.clicked.connect(self.lineupChange)
#         self.nextGymnast1 = QPushButton("Next Gymnast")
#         topButtons1.addWidget(self.nextGymnast1)
#
#         topButtons2 = QHBoxLayout()
#         self.update2 = QPushButton("Update Lineup")
#         topButtons2.addWidget(self.update2)
#         self.update2.clicked.connect(self.lineupChange)
#         self.nextGymnast2 = QPushButton("Next Gymnast")
#         topButtons2.addWidget(self.nextGymnast2)
#
#         topButtons3 = QHBoxLayout()
#         self.update3 = QPushButton("Update Lineup")
#         topButtons3.addWidget(self.update3)
#         self.update3.clicked.connect(self.lineupChange)
#         self.nextGymnast3 = QPushButton("Next Gymnast")
#         topButtons3.addWidget(self.nextGymnast3)
#
#         topButtons4 = QHBoxLayout()
#         self.update4 = QPushButton("Update Lineup")
#         topButtons4.addWidget(self.update4)
#         self.update4.clicked.connect(self.lineupChange)
#         self.nextGymnast4 = QPushButton("Next Gymnast")
#         topButtons4.addWidget(self.nextGymnast4)
#
#         # create 'next event' and 'finish meet' buttons
#         nextButtons = QHBoxLayout()
#         self.nextEvent = QPushButton("Next Event")
#         nextButtons.addWidget(self.nextEvent)
#         self.finish = QPushButton("Finish Meet")
#         nextButtons.addWidget(self.finish)
#         self.finish.clicked.connect(self.meetDone)
#
#         # add areas to each grid layout for each team
#         # ~team 1~
#         team1 = QGridLayout()
#         team1.addLayout(scoreInfo1, 0, 0)
#         team1.addWidget(self.timer1, 1, 0)
#         team1.addLayout(outOrder1, 0, 1, 2, 1)
#         team1.addLayout(topButtons1, 0, 2)
#         mainLayout.addLayout(team1)
#
#         # ~team 2~
#         team2 = QGridLayout()
#         team2.addLayout(scoreInfo2, 0, 0)
#         team2.addWidget(self.timer2, 1, 0)
#         team2.addLayout(outOrder2, 0, 1, 2, 1)
#         team2.addLayout(topButtons2, 0, 2)
#         mainLayout.addLayout(team2)
#
#         # ~team 3~
#         team3 = QGridLayout()
#         if screensController.meetFormat == "Tri" or screensController.meetFormat == "Quad":
#             team3.addLayout(scoreInfo3, 0, 0)
#             team3.addWidget(self.timer3, 1, 0)
#             team3.addLayout(outOrder3, 0, 1, 2, 1)
#             team3.addLayout(topButtons3, 0, 2)
#         mainLayout.addLayout(team3)
#
#         # ~team 4~
#         team4 = QGridLayout()
#         if screensController.meetFormat == "Quad":
#             team4.addLayout(scoreInfo4, 0, 0)
#             team4.addWidget(self.timer4, 1, 0)
#             team4.addLayout(outOrder4, 0, 1, 2, 1)
#             team4.addLayout(topButtons4, 0, 2)
#         mainLayout.addLayout(team4)
#
#         # add 'next event' and 'finish meet' buttons to main layout
#         mainLayout.addLayout(nextButtons)
#
#         # set the main layout on the application's window
#         self.setLayout(mainLayout)
#
#     def update_Score(self, score, team):
#         print(float(score))
#         screensController.update_score(team, float(score))
#
#     def lineupChange(self):
#         updateController.open_window()
#
#     def meetDone(self):
#         screensController.close_windows()
#         postController.open_window()
#
#     def activated1(self):
#         self.orderSelect1.setCurrentIndex(1)
#
#     def activated2(self):
#         self.orderSelect2.setCurrentIndex(1)
#
#     def activated3(self):
#         self.orderSelect3.setCurrentIndex(1)
#
#     def activated4(self):
#         self.orderSelect4.setCurrentIndex(1)
#
#
# class ScorekeeperScreen(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Scorekeeper Screen")
#
#         # create a QVBoxLayout instance for the outer layout
#         mainLayout = QVBoxLayout()
#         self.data = MeetData.get_data()
#
#         # create area for score entering for each team
#         scoreInfo1 = QVBoxLayout()
#         self.schoolName1 = QLabel(self.data.schools[0].school_name)
#         self.schoolName1.setFont(QFont('Arial', 12))
#         scoreInfo1.addWidget(self.schoolName1)
#         self.name1 = QLabel("Gymnast Name")
#         self.name1.setFont(QFont('Arial', 15))
#         scoreInfo1.addWidget(self.name1)
#         self.enterScore1 = QLineEdit()
#         self.enterScore1.setFixedWidth(300)
#         self.enterScore1.setValidator(QDoubleValidator())
#         self.enterScore1.setMaxLength(6)
#         self.enterScore1.setAlignment(Qt.AlignLeft)
#         self.enterScore1.setFont(QFont('Arial', 15))
#         self.enterScore1.returnPressed.connect(lambda: self.update_Score(self.enterScore1.text(), 1))
#         # self.enterScore1.returnPressed.connect(lambda: self.enterPressed())
#         scoreForm1 = QFormLayout()
#         scoreForm1.addRow("Enter Score", self.enterScore1)
#         scoreInfo1.addLayout(scoreForm1)
#
#         scoreInfo2 = QVBoxLayout()
#         self.schoolName2 = QLabel(screensController.competingSchools[1].school_name)
#         self.schoolName2.setFont(QFont('Arial', 12))
#         scoreInfo2.addWidget(self.schoolName2)
#         self.name2 = QLabel("Gymnast Name")
#         self.name2.setFont(QFont('Arial', 15))
#         scoreInfo2.addWidget(self.name2)
#         self.enterScore2 = QLineEdit()
#         self.enterScore2.setFixedWidth(300)
#         self.enterScore2.setValidator(QDoubleValidator())
#         self.enterScore2.setMaxLength(6)
#         self.enterScore2.setAlignment(Qt.AlignLeft)
#         self.enterScore2.setFont(QFont('Arial', 15))
#         self.enterScore2.returnPressed.connect(lambda: self.update_Score(self.enterScore2.text(), 2))
#         # self.enterScore2.returnPressed.connect(lambda: self.enterPressed())
#         scoreForm2 = QFormLayout()
#         scoreForm2.addRow("Enter Score", self.enterScore2)
#         scoreInfo2.addLayout(scoreForm2)
#
#         scoreInfo3 = QVBoxLayout()
#         self.schoolName3 = QLabel(screensController.competingSchools[2].school_name)
#         self.schoolName3.setFont(QFont('Arial', 12))
#         scoreInfo3.addWidget(self.schoolName3)
#         self.name3 = QLabel("Gymnast Name")
#         self.name3.setFont(QFont('Arial', 15))
#         scoreInfo3.addWidget(self.name3)
#         self.enterScore3 = QLineEdit()
#         self.enterScore3.setFixedWidth(300)
#         self.enterScore3.setValidator(QDoubleValidator())
#         self.enterScore3.setMaxLength(6)
#         self.enterScore3.setAlignment(Qt.AlignLeft)
#         self.enterScore3.setFont(QFont('Arial', 15))
#         self.enterScore3.returnPressed.connect(lambda: self.update_Score(self.enterScore3.text(), 3))
#         # self.enterScore3.returnPressed.connect(lambda: self.enterPressed())
#         scoreForm3 = QFormLayout()
#         scoreForm3.addRow("Enter Score", self.enterScore3)
#         scoreInfo3.addLayout(scoreForm3)
#
#         scoreInfo4 = QVBoxLayout()
#         self.schoolName4 = QLabel(screensController.competingSchools[3].school_name)
#         self.schoolName4.setFont(QFont('Arial', 12))
#         scoreInfo4.addWidget(self.schoolName4)
#         self.name4 = QLabel("Gymnast Name")
#         self.name4.setFont(QFont('Arial', 15))
#         scoreInfo4.addWidget(self.name4)
#         self.enterScore4 = QLineEdit()
#         self.enterScore4.setFixedWidth(300)
#         self.enterScore4.setValidator(QDoubleValidator())
#         self.enterScore4.setMaxLength(6)
#         self.enterScore4.setAlignment(Qt.AlignLeft)
#         self.enterScore4.setFont(QFont('Arial', 15))
#         self.enterScore4.returnPressed.connect(lambda: self.update_Score(self.enterScore4.text(), 4))
#         # self.enterScore4.returnPressed.connect(lambda: self.enterPressed())
#         scoreForm4 = QFormLayout()
#         scoreForm4.addRow("Enter Score", self.enterScore4)
#         scoreInfo4.addLayout(scoreForm4)
#
#         # create timer labels for each team
#         self.timer1 = QLabel("--:--")
#         self.timer1.setFont(QFont('Arial', 30))
#         self.timer1.setAlignment(Qt.AlignCenter)
#         self.timer2 = QLabel("--:--")
#         self.timer2.setFont(QFont('Arial', 30))
#         self.timer2.setAlignment(Qt.AlignCenter)
#         self.timer3 = QLabel("--:--")
#         self.timer3.setFont(QFont('Arial', 30))
#         self.timer3.setAlignment(Qt.AlignCenter)
#         self.timer4 = QLabel("--:--")
#         self.timer4.setFont(QFont('Arial', 30))
#         self.timer4.setAlignment(Qt.AlignCenter)
#
#         # create area for out of order selection for each team
#         outOrder1 = QVBoxLayout()
#         self.orderButton1 = QPushButton("Out of Order")
#         self.orderButton1.setCheckable(True)
#         self.orderButton1.toggle()
#         outOrder1.addWidget(self.orderButton1)
#         self.orderSelect1 = QStackedLayout()
#         self.blank1 = QListWidget()
#         self.selection1 = QComboBox()
#         self.selection1.addItems(["Select Next Gymnast...", "Gymnast #1", "Gymnast #2", "Gymnast #3", "Gymnast #4",
#                                   "Gymnast #5", "Gymnast #6"])
#         self.selection1.setFont(QFont('Arial', 10))
#         self.orderSelect1.addWidget(self.blank1)
#         self.orderSelect1.addWidget(self.selection1)
#         self.orderSelect1.setCurrentIndex(0)
#         outOrder1.addLayout(self.orderSelect1)
#
#         outOrder2 = QVBoxLayout()
#         self.orderButton2 = QPushButton("Out of Order")
#         self.orderButton2.setCheckable(True)
#         self.orderButton2.toggle()
#         outOrder2.addWidget(self.orderButton2)
#         self.orderSelect2 = QStackedLayout()
#         self.blank2 = QListWidget()
#         self.selection2 = QComboBox()
#         self.selection2.addItems(["Select Next Gymnast...", "Gymnast #1", "Gymnast #2", "Gymnast #3", "Gymnast #4",
#                                   "Gymnast #5", "Gymnast #6"])
#         self.selection2.setFont(QFont('Arial', 10))
#         self.orderSelect2.addWidget(self.blank2)
#         self.orderSelect2.addWidget(self.selection2)
#         self.orderSelect2.setCurrentIndex(0)
#         outOrder2.addLayout(self.orderSelect2)
#
#         if screensController.meetFormat == "Quad" or screensController.meetFormat == "Tri":
#             outOrder3 = QVBoxLayout()
#             self.orderButton3 = QPushButton("Out of Order")
#             self.orderButton3.setCheckable(True)
#             self.orderButton3.toggle()
#             outOrder3.addWidget(self.orderButton3)
#             self.orderSelect3 = QStackedLayout()
#             self.blank3 = QListWidget()
#             self.selection3 = QComboBox()
#             self.selection3.addItems(["Select Next Gymnast...", "Gymnast #1", "Gymnast #2", "Gymnast #3", "Gymnast #4",
#                                       "Gymnast #5", "Gymnast #6"])
#             self.selection3.setFont(QFont('Arial', 10))
#             self.orderSelect3.addWidget(self.blank3)
#             self.orderSelect3.addWidget(self.selection3)
#             self.orderSelect3.setCurrentIndex(0)
#             self.orderButton3.clicked.connect(self.activated3)
#             outOrder3.addLayout(self.orderSelect3)
#
#         if screensController.meetFormat == "Quad":
#             outOrder4 = QVBoxLayout()
#             self.orderButton4 = QPushButton("Out of Order")
#             self.orderButton4.setCheckable(True)
#             self.orderButton4.toggle()
#             outOrder4.addWidget(self.orderButton4)
#             self.orderSelect4 = QStackedLayout()
#             self.blank4 = QListWidget()
#             self.selection4 = QComboBox()
#             self.selection4.addItems(["Select Next Gymnast...", "Gymnast #1", "Gymnast #2", "Gymnast #3", "Gymnast #4",
#                                       "Gymnast #5", "Gymnast #6"])
#             self.selection4.setFont(QFont('Arial', 10))
#             self.orderSelect4.addWidget(self.blank4)
#             self.orderSelect4.addWidget(self.selection4)
#             self.orderSelect4.setCurrentIndex(0)
#             self.orderButton4.clicked.connect(self.activated4)
#             outOrder4.addLayout(self.orderSelect4)
#
#         # put function to 'out of order' buttons
#         self.orderButton1.clicked.connect(self.activated1)
#         self.orderButton2.clicked.connect(self.activated2)
#
#         # create area for 'update lineup' and 'next gymnast' buttons for each team
#         topButtons1 = QHBoxLayout()
#         self.update1 = QPushButton("Update Lineup")
#         topButtons1.addWidget(self.update1)
#         self.update1.clicked.connect(self.lineupChange)
#         self.nextGymnast1 = QPushButton("Next Gymnast")
#         topButtons1.addWidget(self.nextGymnast1)
#
#         topButtons2 = QHBoxLayout()
#         self.update2 = QPushButton("Update Lineup")
#         topButtons2.addWidget(self.update2)
#         self.update2.clicked.connect(self.lineupChange)
#         self.nextGymnast2 = QPushButton("Next Gymnast")
#         topButtons2.addWidget(self.nextGymnast2)
#
#         topButtons3 = QHBoxLayout()
#         self.update3 = QPushButton("Update Lineup")
#         topButtons3.addWidget(self.update3)
#         self.update3.clicked.connect(self.lineupChange)
#         self.nextGymnast3 = QPushButton("Next Gymnast")
#         topButtons3.addWidget(self.nextGymnast3)
#
#         topButtons4 = QHBoxLayout()
#         self.update4 = QPushButton("Update Lineup")
#         topButtons4.addWidget(self.update4)
#         self.update4.clicked.connect(self.lineupChange)
#         self.nextGymnast4 = QPushButton("Next Gymnast")
#         topButtons4.addWidget(self.nextGymnast4)
#
#         # create 'next event' and 'finish meet' buttons
#         nextButtons = QHBoxLayout()
#         self.nextEvent = QPushButton("Next Event")
#         nextButtons.addWidget(self.nextEvent)
#         self.finish = QPushButton("Finish Meet")
#         nextButtons.addWidget(self.finish)
#         self.finish.clicked.connect(self.meetDone)
#
#         # add areas to each grid layout for each team
#         # ~team 1~
#         team1 = QGridLayout()
#         team1.addLayout(scoreInfo1, 0, 0)
#         team1.addWidget(self.timer1, 1, 0)
#         team1.addLayout(outOrder1, 0, 1, 2, 1)
#         team1.addLayout(topButtons1, 0, 2)
#         mainLayout.addLayout(team1)
#
#         # ~team 2~
#         team2 = QGridLayout()
#         team2.addLayout(scoreInfo2, 0, 0)
#         team2.addWidget(self.timer2, 1, 0)
#         team2.addLayout(outOrder2, 0, 1, 2, 1)
#         team2.addLayout(topButtons2, 0, 2)
#         mainLayout.addLayout(team2)
#
#         # ~team 3~
#         team3 = QGridLayout()
#         if screensController.meetFormat == "Tri" or screensController.meetFormat == "Quad":
#             team3.addLayout(scoreInfo3, 0, 0)
#             team3.addWidget(self.timer3, 1, 0)
#             team3.addLayout(outOrder3, 0, 1, 2, 1)
#             team3.addLayout(topButtons3, 0, 2)
#         mainLayout.addLayout(team3)
#
#         # ~team 4~
#         team4 = QGridLayout()
#         if screensController.meetFormat == "Quad":
#             team4.addLayout(scoreInfo4, 0, 0)
#             team4.addWidget(self.timer4, 1, 0)
#             team4.addLayout(outOrder4, 0, 1, 2, 1)
#             team4.addLayout(topButtons4, 0, 2)
#         mainLayout.addLayout(team4)
#
#         # add 'next event' and 'finish meet' buttons to main layout
#         mainLayout.addLayout(nextButtons)
#
#         # set the main layout on the application's window
#         self.setLayout(mainLayout)
#
#     def update_Score(self, score, team):
#         print(float(score))
#         screensController.update_score(team, float(score))
#
#     def lineupChange(self):
#         updateController.open_window()
#
#     def meetDone(self):
#         screensController.close_windows()
#         postController.open_window()
#
#     def activated1(self):
#         self.orderSelect1.setCurrentIndex(1)
#
#     def activated2(self):
#         self.orderSelect2.setCurrentIndex(1)
#
#     def activated3(self):
#         self.orderSelect3.setCurrentIndex(1)
#
#     def activated4(self):
#         self.orderSelect4.setCurrentIndex(1)
#

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
