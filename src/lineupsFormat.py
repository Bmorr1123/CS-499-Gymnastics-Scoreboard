import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class BlankLineups(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.blankLineups = QVBoxLayout()
        self.blankLabel = QLabel("")
        self.blankLabel.setFont(QFont('Arial', 20))
        self.blankLineups.addWidget(self.blankLabel)
        self.setLayout(self.blankLineups)


class MonoLineup(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.monoLineup = QVBoxLayout()
        self.setLayout(self.monoLineup)

        self.school1 = QPushButton("Select School #1")
        self.insertLineup1 = QPushButton("Insert Lineup #1 File")
        self.insert1Label = QLabel("Lineup #1")
        self.insert1Label.setFont(QFont('Arial', 10))
        self.insertLineup1.clicked.connect(self.getFile)

        self.monoLineup.addWidget(self.school1)
        self.monoLineup.addWidget(self.insertLineup1)
        self.monoLineup.addWidget(self.insert1Label)

    def getFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Text files (*.txt)")
        self.insert1Label.setText(fileName)
        # crashes when user selects a file


class DualLineups(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dualLineups = QVBoxLayout()
        self.setLayout(self.dualLineups)

        self.school2 = QPushButton("Select School #2")
        self.insertLineup2 = QPushButton("Insert Lineup #2 File")
        self.insertLineup2.clicked.connect(self.getFile)
        self.insert2Label = QLabel("Lineup #2")
        self.insert2Label.setFont(QFont('Arial', 10))

        self.dualLineups.addWidget(self.school2)
        self.dualLineups.addWidget(self.insertLineup2)
        self.dualLineups.addWidget(self.insert2Label)

    def getFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Text files (*.txt)")
        self.insert2Label.setText(fileName)
        # crashes when user selects a file


class TriLineups(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.triLineups = QVBoxLayout()
        self.setLayout(self.triLineups)

        self.school3 = QPushButton("Select School #3")
        self.insertLineup3 = QPushButton("Insert Lineup #3 File")
        self.insertLineup3.clicked.connect(self.getFile)
        self.insert3Label = QLabel("Lineup #3")
        self.insert3Label.setFont(QFont('Arial', 10))

        self.triLineups.addWidget(self.school3)
        self.triLineups.addWidget(self.insertLineup3)
        self.triLineups.addWidget(self.insert3Label)

    def getFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Text files (*.txt)")
        self.insert3Label.setText(fileName)
        # crashes when user selects a file


class QuadLineups(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quadLineups = QVBoxLayout()
        self.setLayout(self.quadLineups)

        self.school4 = QPushButton("Select School #4")
        self.insertLineup4 = QPushButton("Insert Lineup #4 File")
        self.insertLineup4.clicked.connect(self.getFile)
        self.insert4Label = QLabel("Lineup #4")
        self.insert4Label.setFont(QFont('Arial', 10))

        self.quadLineups.addWidget(self.school4)
        self.quadLineups.addWidget(self.insertLineup4)
        self.quadLineups.addWidget(self.insert4Label)

    def getFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "Text files (*.txt)")
        self.insert4Label.setText(fileName)
        # crashes when user selects a file