import sys

import setupController
import screensController

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from lineupsFormat import *


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
        self.lineupsFormat = QVBoxLayout()  # layout that holds insertion buttons
        self.lineup1 = QStackedLayout()
        self.lineup2 = QStackedLayout()
        self.lineup3 = QStackedLayout()
        self.lineup4 = QStackedLayout()

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
        self.dualButton.toggled.connect(lambda: self.changeLineups(self.dualButton))
        self.formatButtons.addWidget(self.dualButton)
        self.triButton = QRadioButton("Triangular")
        self.triButton.setChecked(False)
        self.triButton.toggled.connect(lambda: self.changeLineups(self.triButton))
        self.formatButtons.addWidget(self.triButton)
        self.quadButton = QRadioButton("Quadrangular")
        self.quadButton.setChecked(False)
        self.quadButton.toggled.connect(lambda: self.changeLineups(self.quadButton))
        self.formatButtons.addWidget(self.quadButton)
        self.formatSelect.addLayout(self.formatButtons)

        # create & add necessary widgets/layouts to lineups insertion layout
        lineupsTitle = QLabel("Team Lineups")
        lineupsTitle.setFont(QFont('Arial', 10))
        lineupsTitle.setAlignment(Qt.AlignCenter)
        self.lineupsInsert.addWidget(lineupsTitle)

        self.lineup1.addWidget(BlankLineups())
        self.lineup1.addWidget(MonoLineup())
        self.lineup1.setCurrentIndex(0)
        self.lineupsFormat.addLayout(self.lineup1)

        self.lineup2.addWidget(BlankLineups())
        self.lineup2.addWidget(DualLineups())
        self.lineup2.setCurrentIndex(0)
        self.lineupsFormat.addLayout(self.lineup2)

        self.lineup3.addWidget(BlankLineups())
        self.lineup3.addWidget(TriLineups())
        self.lineup3.setCurrentIndex(0)
        self.lineupsFormat.addLayout(self.lineup3)

        self.lineup4.addWidget(BlankLineups())
        self.lineup4.addWidget(QuadLineups())
        self.lineup4.setCurrentIndex(0)
        self.lineupsFormat.addLayout(self.lineup4)
        self.lineupsInsert.addLayout(self.lineupsFormat)

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
        self.setLayout(gridFormat)

    def doneClicked(self):
        format = ""
        if self.triButton.isChecked():
            format = "Tri"
        elif self.quadButton.isChecked():
            format = "Quad"
        setupController.close_window()
        screensController.open_windows(self.logoCheckbox.isChecked(), self.orderCheckbox.isChecked(),
                                       self.svCheckbox.isChecked(), self.judgesCheckbox.isChecked(), format)

    def resetSelections(self):
        self.logoCheckbox.setChecked(False)
        self.orderCheckbox.setChecked(False)
        self.svCheckbox.setChecked(False)
        self.judgesCheckbox.setChecked(False)

        self.dualButton.setChecked(False)
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
        else:
            self.judgesLabel.setText("List of Judges")

    def changeLineups(self, button):
        if button.text() == "Dual":
            if button.isChecked():
                self.lineup1.setCurrentIndex(1)
                self.lineup2.setCurrentIndex(1)
                self.lineup3.setCurrentIndex(0)
                self.lineup4.setCurrentIndex(0)

        if button.text() == "Triangular":
            if button.isChecked():
                self.lineup1.setCurrentIndex(1)
                self.lineup2.setCurrentIndex(1)
                self.lineup3.setCurrentIndex(1)
                self.lineup4.setCurrentIndex(0)

        if button.text() == "Quadrangular":
            if button.isChecked():
                self.lineup1.setCurrentIndex(1)
                self.lineup2.setCurrentIndex(1)
                self.lineup3.setCurrentIndex(1)
                self.lineup4.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

