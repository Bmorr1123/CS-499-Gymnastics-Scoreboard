import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SchoolSelection(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Schools")

        schools = QVBoxLayout()
        self.selectTitle = QLabel("Select School")
        self.selectTitle.setFont(QFont('Arial', 10))
        self.selectTitle.setAlignment(Qt.AlignCenter)
        schools.addWidget(self.selectTitle)

        self.schoolList = QListWidget()
        QListWidgetItem("LSU", self.schoolList)
        QListWidgetItem("MSU", self.schoolList)
        QListWidgetItem("BAMA", self.schoolList)
        QListWidgetItem("AUBURN", self.schoolList)
        schools.addWidget(self.schoolList)

        self.setLayout(schools)
