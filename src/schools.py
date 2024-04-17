import sys
import json_management

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import setupController


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
        json_management.load_teams_from_directory(setupController.db_int, "../resources/teams")
        for school in setupController.db_int.get_schools():
            QListWidgetItem(school.school_name, self.schoolList)
        schools.addWidget(self.schoolList)

        self.setLayout(schools)
