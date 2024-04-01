import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Setup Screen")

        # create a QGridLayout instance for outer layout
        gridFormat = QGridLayout()

        # create inner layout instances for widgets
        self.customization = QVBoxLayout()  # customization section layout
        self.customizeCheckboxes = QVBoxLayout()  # checkboxes layout for customization

        self.formatSelect = QVBoxLayout()  # meet format selection layout
        self.formatButtons = QHBoxLayout()  # meet format buttons layout

        self.lineupsInsert = QVBoxLayout()  # team lineups insertion layout
        #self.blankLineups = QVBoxLayout()  # blank layout for when no meet format has been chosen
        #self.dualLineups = QVBoxLayout()  # lineup layout for dual meet
        #self.triLineups = QVBoxLayout()  # lineup layout for triangular meet
        #self.quadLineups = QVBoxLayout()  # lineup layout for quadrangular meet

        self.judgesInsert = QVBoxLayout()  # judges insertion layout

        self.otherButtons = QHBoxLayout()  # "reset selection" and "setup done" button layout

        # add inner layouts to outer layouts
        gridFormat.addLayout(self.customization, 0, 0)
        gridFormat.addLayout(self.formatSelect, 0, 1)
        gridFormat.addLayout(self.lineupsInsert, 1, 0)
        gridFormat.addLayout(self.judgesInsert, 1, 1)
        gridFormat.addLayout(self.otherButtons, 2, 1)

        # create & add necessary widgets/layouts to customization layout
        customizationTitle = QLabel("Customization")
        customizationTitle.setFont(QFont('Arial', 10))
        customizationTitle.setAlignment(Qt.AlignCenter)
        self.customization.addWidget(customizationTitle)

        self.logoCheckbox = QCheckBox("Display Logos")
        self.logoCheckbox.setChecked(False)
        self.customizeCheckboxes.addWidget(self.logoCheckbox)
        self.orderCheckbox = QCheckBox("Display Order")
        self.orderCheckbox.setChecked(False)
        self.customizeCheckboxes.addWidget(self.orderCheckbox)
        self.svCheckbox = QCheckBox("Display Start Value")
        self.svCheckbox.setChecked(False)
        self.customizeCheckboxes.addWidget(self.svCheckbox)
        self.judgesCheckbox = QCheckBox("Display Judges")
        self.judgesCheckbox.setChecked(False)
        self.customizeCheckboxes.addWidget(self.judgesCheckbox)
        self.customization.addLayout(self.customizeCheckboxes)

        # create & add necessary widgets/layouts to meet format select layout
        formatTitle = QLabel("Meet Format")
        formatTitle.setFont(QFont('Arial', 10))
        formatTitle.setAlignment(Qt.AlignCenter)
        self.formatSelect.addWidget(formatTitle)

        self.dualButton = QRadioButton("Dual")
        self.dualButton.setChecked(False)
        self.formatButtons.addWidget(self.dualButton)
        self.triButton = QRadioButton("Triangular")
        self.triButton.setChecked(False)
        self.formatButtons.addWidget(self.triButton)
        self.quadButton = QRadioButton("Quadrangular")
        self.quadButton.setChecked(False)
        self.formatButtons.addWidget(self.quadButton)
        self.formatSelect.addLayout(self.formatButtons)

        # create & add necessary widgets/layouts to lineups insertion layout
        lineupsTitle = QLabel("Team Lineups")
        lineupsTitle.setFont(QFont('Arial', 10))
        lineupsTitle.setAlignment(Qt.AlignCenter)
        self.lineupsInsert.addWidget(lineupsTitle)

        # NEED TO ADD FUNCTION TO BUTTONS (pop up new window... maybe?)
        self.school1 = QPushButton("Select School #1")
        self.school2 = QPushButton("Select School #2")
        self.school3 = QPushButton("Select School #3")
        self.school4 = QPushButton("Select School #4")

        self.insertLineup1 = QPushButton("Insert Lineup #1 File")
        self.insertLineup1.clicked.connect(self.getFile)
        self.insert1Label = QLabel("Lineup #1")
        self.insert1Label.setFont(QFont('Arial', 10))
        self.insertLineup2 = QPushButton("Insert Lineup #2 File")
        self.insertLineup2.clicked.connect(self.getFile)
        self.insert2Label = QLabel("Lineup #2")
        self.insert2Label.setFont(QFont('Arial', 10))
        self.insertLineup3 = QPushButton("Insert Lineup #3 File")
        self.insertLineup3.clicked.connect(self.getFile)
        self.insert3Label = QLabel("Lineup #3")
        self.insert3Label.setFont(QFont('Arial', 10))
        self.insertLineup4 = QPushButton("Insert Lineup #4 File")
        self.insertLineup4.clicked.connect(self.getFile)
        self.insert4Label = QLabel("Lineup #4")
        self.insert4Label.setFont(QFont('Arial', 10))

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        self.stack4UI()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        self.Stack.addWidget(self.stack4)

        self.lineupsInsert.addWidget(self.Stack)
        self.Stack.setCurrentIndex(0)  # NOT SHOWING BUTTONS!!!!!

        # create & add necessary widgets to judges insertion layout
        judgesTitle = QLabel("Judges")
        judgesTitle.setFont(QFont('Arial', 10))
        judgesTitle.setAlignment(Qt.AlignCenter)
        self.judgesInsert.addWidget(judgesTitle)

        self.judgeInButton = QPushButton("Insert File of Judges")
        self.judgeInButton.clicked.connect(self.getFile)
        self.judgesInsert.addWidget(self.judgeInButton)
        self.judgesLabel = QLabel("List of Judges")
        self.judgesLabel.setFont(QFont('Arial', 10))
        self.judgesInsert.addWidget(self.judgesLabel)

        # create & add necessary widgets to the other buttons layout
        self.resetButton = QPushButton("Reset Selections")
        self.resetButton.clicked.connect(self.resetSelections)
        self.otherButtons.addWidget(self.resetButton)
        self.doneButton = QPushButton("Finish Setup")
        # NEED TO ADD FUNCTION ONCE SCOREKEEPER IS DONE
        self.otherButtons.addWidget(self.doneButton)

        # set the main layout on the application's window
        self.setLayout(gridFormat)

    def getFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Text files (*.txt)")
        self.judgesLabel.setText(fileName)
        # crashes when user does not select a file

    def resetSelections(self):
        self.logoCheckbox.setChecked(False)
        self.orderCheckbox.setChecked(False)
        self.svCheckbox.setChecked(False)
        self.judgesCheckbox.setChecked(False)

        self.dualButton.setChecked(False)
        self.triButton.setChecked(False)
        self.quadButton.setChecked(False)

        self.lineupsFormat.setCurrentIndex(0)

        self.judgesLabel.setText("List of Judges")

    def stack1UI(self):
        self.blankLineups = QVBoxLayout()  # blank layout for when no meet format has been chosen
        self.stack1.setLayout(self.blankLineups)

    def stack2UI(self):
        self.dualLineups = QVBoxLayout()  # lineup layout for dual meet
        self.dualLineups.addWidget(self.school1)
        self.dualLineups.addWidget(self.insertLineup1)
        self.dualLineups.addWidget(self.insert1Label)
        self.dualLineups.addWidget(self.school2)
        self.dualLineups.addWidget(self.insertLineup2)
        self.dualLineups.addWidget(self.insert2Label)
        self.stack2.setLayout(self.dualLineups)

    def stack3UI(self):
        self.triLineups = QVBoxLayout()  # lineup layout for triangular meet
        self.triLineups.addWidget(self.school1)
        self.triLineups.addWidget(self.insertLineup1)
        self.triLineups.addWidget(self.insert1Label)
        self.triLineups.addWidget(self.school2)
        self.triLineups.addWidget(self.insertLineup2)
        self.triLineups.addWidget(self.insert2Label)
        self.triLineups.addWidget(self.school3)
        self.triLineups.addWidget(self.insertLineup3)
        self.triLineups.addWidget(self.insert3Label)
        self.stack3.setLayout(self.triLineups)

    def stack4UI(self):
        self.quadLineups = QVBoxLayout()  # lineup layout for quadrangular meet
        self.quadLineups.addWidget(self.school1)
        self.quadLineups.addWidget(self.insertLineup1)
        self.quadLineups.addWidget(self.insert1Label)
        self.quadLineups.addWidget(self.school2)
        self.quadLineups.addWidget(self.insertLineup2)
        self.quadLineups.addWidget(self.insert2Label)
        self.quadLineups.addWidget(self.school3)
        self.quadLineups.addWidget(self.insertLineup3)
        self.quadLineups.addWidget(self.insert3Label)
        self.quadLineups.addWidget(self.school4)
        self.quadLineups.addWidget(self.insertLineup4)
        self.quadLineups.addWidget(self.insert4Label)
        self.stack4.setLayout(self.quadLineups)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

