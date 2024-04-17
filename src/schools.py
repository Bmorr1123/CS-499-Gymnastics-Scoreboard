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
        for school in setupController.db_int.get_schools():
            QListWidgetItem(school.school_name, self.schoolList)
        schools.addWidget(self.schoolList)
        self.schoolList.itemClicked.connect(self.school_clicked)

        self.setLayout(schools)

    def school_clicked(self, clicked_item):
        print(clicked_item.text())
        setupController.schools_selected.append(setupController.db_int.get_school_by_name(clicked_item.text()))
