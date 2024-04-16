import sys

import postController

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Post Meet Screen")

        # create a QHBoxLayout instance (for side-by-side placements)
        placements = QGridLayout()
        placements.setRowStretch(1, 1)

        # create a QVBoxLayout instance for each type of placement (final and all-around)
        finalScores = QVBoxLayout()
        finalScores.setContentsMargins(60, 0, 0, 0)
        aroundScores = QVBoxLayout()
        aroundScores.setContentsMargins(60, 0, 0, 0)

        # create score titles
        finalTitle = QLabel("Final Team Placements")
        finalTitle.setFont(QFont('Arial', 50))
        finalTitle.setAlignment(Qt.AlignCenter)
        aroundTitle = QLabel("All-Around Placements")
        aroundTitle.setFont(QFont('Arial', 50))
        aroundTitle.setAlignment(Qt.AlignCenter)

        # create labels for final meet scores
        finalScore1 = QLabel("1st: " + "Team Name " + str(postController.sortedScores[0]))
        finalScore1.setFont(QFont('Arial', 50))
        finalScore2 = QLabel("2nd: " + "Team Name " + str(postController.sortedScores[1]))
        finalScore2.setFont(QFont('Arial', 50))
        finalScore3 = QLabel("3rd: " + "Team Name " + str(postController.sortedScores[2]))
        finalScore3.setFont(QFont('Arial', 50))
        finalScore4 = QLabel("4th: " + "Team Name " + str(postController.sortedScores[3]))
        finalScore4.setFont(QFont('Arial', 50))

        # create labels for all-around scores
        aroundScore1 = QLabel("1st: " + "Jane Doe " + "38.99")
        aroundScore1.setFont(QFont('Arial', 50))
        aroundScore2 = QLabel("2nd: " + "Jane Doe " + "38.99")
        aroundScore2.setFont(QFont('Arial', 50))
        aroundScore3 = QLabel("3rd: " + "Jane Doe " + "38.99")
        aroundScore3.setFont(QFont('Arial', 50))

        # add titles to outer layout
        placements.addWidget(finalTitle, 0, 0)
        placements.addWidget(aroundTitle, 0, 1)

        # add score layouts to placements format layout
        placements.addLayout(finalScores, 1, 0)
        placements.addLayout(aroundScores, 1, 1)

        # add widgets to inner score layouts
        # ~final scores~
        finalScores.addWidget(finalScore1)
        finalScores.addWidget(finalScore2)
        if True:
            finalScores.addWidget(finalScore3)
        if True:
            finalScores.addWidget(finalScore4)

        # ~all-around scores~
        aroundScores.addWidget(aroundScore1)
        aroundScores.addWidget(aroundScore2)
        aroundScores.addWidget(aroundScore3)

        # set the layout on the application's window
        self.setLayout(placements)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
