import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lineup Substitution")

        # create a QVBoxLayout instance
        substitution = QVBoxLayout()

        # create inner layouts for substitutions
        selectLineups = QVBoxLayout()
        subLineups = QGridLayout()
        self.teamLineup = QStackedLayout()
        self.teamRoster = QStackedLayout()

        # create substitution title for window
        subTitle = QLabel("Lineup Substitution")
        subTitle.setFont(QFont('Arial', 30))
        subTitle.setAlignment(Qt.AlignCenter)

        # create dropdown menu for lineups
        selectTitle = QLabel("Select Lineup To Update:")
        selectTitle.setFont(QFont('Arial', 20))
        selectTitle.setAlignment(Qt.AlignCenter)
        lineupMenu = QComboBox()
        lineupMenu.addItems(["Select Lineup...", "Lineup #1", "Lineup #2", "Lineup #3", "Lineup #4"])
        lineupMenu.setFont(QFont('Arial', 15))

        # add lineup dropdown to inner layout
        selectLineups.addWidget(selectTitle)
        selectLineups.addWidget(lineupMenu)

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
        available1 = QListWidget()
        QListWidgetItem("Gymnast A1", available1)
        QListWidgetItem("Gymnast B1", available1)
        QListWidgetItem("Gymnast C1", available1)
        QListWidgetItem("Gymnast D1", available1)
        QListWidgetItem("Gymnast E1", available1)
        available1.setFont(QFont('Arial', 15))

        # ~team 2~
        available2 = QListWidget()
        QListWidgetItem("Gymnast A2", available2)
        QListWidgetItem("Gymnast B2", available2)
        QListWidgetItem("Gymnast C2", available2)
        QListWidgetItem("Gymnast D2", available2)
        QListWidgetItem("Gymnast E2", available2)
        available2.setFont(QFont('Arial', 15))

        # ~team 3~
        available3 = QListWidget()
        QListWidgetItem("Gymnast A3", available3)
        QListWidgetItem("Gymnast B3", available3)
        QListWidgetItem("Gymnast C3", available3)
        QListWidgetItem("Gymnast D3", available3)
        QListWidgetItem("Gymnast E3", available3)
        available3.setFont(QFont('Arial', 15))

        # ~team 4~
        available4 = QListWidget()
        QListWidgetItem("Gymnast A4", available4)
        QListWidgetItem("Gymnast B4", available4)
        QListWidgetItem("Gymnast C4", available4)
        QListWidgetItem("Gymnast D4", available4)
        QListWidgetItem("Gymnast E4", available4)
        available4.setFont(QFont('Arial', 15))

        # add available gymnasts for each team to stacked layout
        self.teamLineup.addWidget(blank1)
        self.teamLineup.addWidget(available1)
        self.teamLineup.addWidget(available2)
        self.teamLineup.addWidget(available3)
        self.teamLineup.addWidget(available4)
        self.teamLineup.setCurrentIndex(0)

        # create team rosters
        # ~team 1~
        roster1 = QListWidget()
        QListWidgetItem("Available A1", roster1)
        QListWidgetItem("Available B1", roster1)
        QListWidgetItem("Available C1", roster1)
        QListWidgetItem("Available D1", roster1)
        QListWidgetItem("Available E1", roster1)
        roster1.setFont(QFont('Arial', 15))

        # ~team 2~
        roster2 = QListWidget()
        QListWidgetItem("Available A2", roster2)
        QListWidgetItem("Available B2", roster2)
        QListWidgetItem("Available C2", roster2)
        QListWidgetItem("Available D2", roster2)
        QListWidgetItem("Available E2", roster2)
        roster2.setFont(QFont('Arial', 15))

        # ~team 3~
        roster3 = QListWidget()
        QListWidgetItem("Available A3", roster3)
        QListWidgetItem("Available B3", roster3)
        QListWidgetItem("Available C3", roster3)
        QListWidgetItem("Available D3", roster3)
        QListWidgetItem("Available E3", roster3)
        roster3.setFont(QFont('Arial', 15))

        # ~team 4~
        roster4 = QListWidget()
        QListWidgetItem("Available A4", roster4)
        QListWidgetItem("Available B4", roster4)
        QListWidgetItem("Available C4", roster4)
        QListWidgetItem("Available D4", roster4)
        QListWidgetItem("Available E4", roster4)
        roster4.setFont(QFont('Arial', 15))

        # add team rosters for each team to stacked layout
        self.teamRoster.addWidget(blank2)
        self.teamRoster.addWidget(roster1)
        self.teamRoster.addWidget(roster2)
        self.teamRoster.addWidget(roster3)
        self.teamRoster.addWidget(roster4)
        self.teamRoster.setCurrentIndex(0)

        # add substitution mechanic to inner layout
        subLineups.addWidget(selectGymnasts, 0, 0)
        subLineups.addWidget(selectSubstitution, 0, 1)
        subLineups.addLayout(self.teamLineup, 1, 0)
        subLineups.addLayout(self.teamRoster, 1, 1)

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
        lineupMenu.activated.connect(self.activated)

        # set the layout on the application's window
        self.setLayout(substitution)

    def activated(self, index):
        self.teamLineup.setCurrentIndex(index)
        self.teamRoster.setCurrentIndex(index)

    def updateClicked(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
