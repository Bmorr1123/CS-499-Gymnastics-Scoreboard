import os
import sys

from PyQt5.QtWidgets import (QApplication, QGridLayout, QPushButton, QWidget, QHBoxLayout, QLabel, )
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

import db.models
from db_interface import DBInterface
from data import MeetData
from models import Gymnast
from pickle import loads


class TeamLayout(QGridLayout):
    def __init__(
            self,
            team_number: int
    ):
        super().__init__()
        self.team_number = team_number
        self.db_interface = DBInterface.get_interface()
        self.data = MeetData.get_data()
        self.school = self.db_interface.get_school_by_name(self.data.schools[self.team_number])[0]
        self.event_lineup_manager = self.data.event_lineup_managers[self.team_number]

        self.display_settings = self.data.display_settings

        self.image_score_layout = QHBoxLayout()
        self.score_color_index = 0
        self.score_label = QLabel("0.00")
        self.score_label.setFont(QFont('Arial', 50))
        self.score_label.setAlignment(Qt.AlignCenter)
        if self.display_settings.display_logo:
            self.logo_label = QLabel()
            self.logo_label.pixmap = QPixmap('exampleLogo.jpg')  # will need to transfer school logo in
            self.logo_label.setPixmap(self.logo_label.pixmap.scaled(150, 150))
            self.logo_label.setAlignment(Qt.AlignCenter)
            self.image_score_layout.addWidget(self.logo_label, 1)
        self.info_layout = QVBoxLayout()
        self.name_label = QLabel(f"Gymnast Name")
        self.name_label.setFont(QFont('Arial', 20))
        self.classification_label = QLabel("Classification")
        self.classification_label.setFont(QFont('Arial', 15))
        self.major_label = QLabel("Major")
        self.major_label.setFont(QFont('Arial', 15))
        self.season_avg_label = QLabel("Season Average")
        self.season_avg_label.setFont(QFont('Arial', 15))
        self.gymnast_image_label = QLabel()
        self.gymnast_image_label.pixmap = QPixmap()  # will need to transfer current gymnast pic in

        self.gymnast_image_label.setPixmap(self.gymnast_image_label.pixmap.scaled(150, 150))
        self.gymnast_image_label.setAlignment(Qt.AlignCenter)
        self.order_label = QLabel("Order: " + "1st")  # will need to be replaced with attribute
        self.order_label.setFont(QFont('Arial', 30))
        self.order_label.setAlignment(Qt.AlignCenter)
        self.apparatus_layout = QHBoxLayout()
        self.apparatus_label = QLabel("VT")
        self.apparatus_label.setFont(QFont('Arial', 20))
        self.apparatus_label.setAlignment(Qt.AlignCenter)

        if self.display_settings.display_start_value:
            self.start_value_label = QLabel("SV")
            self.start_value_label.setFont(QFont('Arial', 20))
            self.start_value_label.setAlignment(Qt.AlignCenter)
            self.apparatus_layout.addWidget(self.start_value_label)
        self.vault_name_label = QLabel("Vault Name")
        self.vault_name_label.setFont(QFont('Arial', 15))
        self.judges_layout = QVBoxLayout()

        if self.display_settings.display_judges:
            self.judge_title_label = QLabel("Judges: ")
            self.judge_title_label.setFont(QFont('Arial', 10))
            self.judge_label_1 = QLabel("Judge 1")
            self.judge_label_1.setFont(QFont('Arial', 10))
            self.judge_label_2 = QLabel("Judge 2")
            self.judge_label_2.setFont(QFont('Arial', 10))
            self.judge_label_3 = QLabel("Judge 3")
            self.judge_label_3.setFont(QFont('Arial', 10))
            self.judges_layout.addWidget(self.judge_title_label)
            self.judges_layout.addWidget(self.judge_label_1)
            self.judges_layout.addWidget(self.judge_label_2)
            self.judges_layout.addWidget(self.judge_label_3)
        self.timer_label = QLabel("--:--")
        self.timer_label.setFont(QFont('Arial', 40))
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.addLayout(self.image_score_layout, 0, 0, 1, 3)
        self.image_score_layout.addWidget(self.score_label, 2)
        self.addLayout(self.info_layout, 1, 0, 1, 1)
        self.info_layout.addWidget(self.name_label)
        self.info_layout.addWidget(self.classification_label)
        self.info_layout.addWidget(self.major_label)
        self.info_layout.addWidget(self.season_avg_label)
        self.addWidget(self.gymnast_image_label, 1, 1)

        if self.display_settings.display_order:
            self.addWidget(self.order_label, 1, 2)

        self.addLayout(self.apparatus_layout, 2, 0, 1, 2)
        self.apparatus_layout.addWidget(self.apparatus_label)
        self.addWidget(self.vault_name_label, 3, 0, 1, 2)
        self.addLayout(self.judges_layout, 2, 2, 2, 1)
        self.addWidget(self.timer_label, 4, 0, 1, 3)

        self.flash_timer = QTimer(self)
        self.stop_timer = QTimer(self)
        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self.refresh_ui)
        self.last_gymnast = None
        self.last_score = None
        self.refresh_ui()

    def get_current_gymnast(self) -> Gymnast | None:
        gymnast_id = self.event_lineup_manager.get_current_gymnast_id()
        gymnasts = self.db_interface.get_gymnast_by_id(gymnast_id)
        return gymnasts[0] if len(gymnasts) == 1 else None

    def populate_empty_fields(self):
        self.score_label.setText("0.00")
        self.gymnast_image_label.setPixmap(QPixmap())
        self.name_label.setText(f"Gymnast Name")
        self.classification_label.setText("Classification")
        self.major_label.setText("Major")
        self.season_avg_label.setText("Season Avg: N/A")
        self.order_label.setText("Order: " + "N/A")
        self.apparatus_label.setText("No Apparatus")
        if self.display_settings.display_start_value:
            self.start_value_label.setText("SV")
        self.vault_name_label.setText("Vault Name")
        current_apparatus = self.event_lineup_manager.get_current_apparatus_name()
        if current_apparatus:
            self.apparatus_label.setText(current_apparatus)
        if self.display_settings.display_judges:
            self.judge_title_label.setText("Judges: ")
            self.judge_label_1.setText("Judge 1")
            self.judge_label_2.setText("Judge 2")
            self.judge_label_3.setText("Judge 3")
        # self.timer_label.setText("--:--")

    def load_gymnast_information(self):
        gymnast = self.get_current_gymnast()
        if not gymnast:
            self.populate_empty_fields()
            return
        if gymnast == self.last_gymnast:
            return
        if gymnast.gymnast_picture_path:
            try:
                qimage = QImage(gymnast.gymnast_picture_path)
                # with open(, "rb") as file:
                #     qimage = QImage
                # print(gymnast.gymnast_picture_path)
                self.gymnast_image_label.pixmap = QPixmap(gymnast.gymnast_picture_path)
                self.gymnast_image_label.setPixmap(self.gymnast_image_label.pixmap.scaled(150, 150))
                self.gymnast_image_label.setAlignment(Qt.AlignCenter)
                # .fromImage(qimage, flags=None)
            except Exception as e:
                print("EXCEPTION:", e)
        self.name_label.setText(f"{gymnast.first_name} {gymnast.last_name}")
        self.classification_label.setText(f"{gymnast.classification}")
        self.major_label.setText(f"{gymnast.major}")

        current_apparatus = self.event_lineup_manager.get_current_apparatus_name()
        self.apparatus_label.setText(current_apparatus)
        if current_apparatus == "Bars":
            self.season_avg_label.setText(f"Season Avg: {gymnast.bars_avg:.03f}")
        elif current_apparatus == "Beam":
            self.season_avg_label.setText(f"Season Avg: {gymnast.beam_avg:.03f}")
        elif current_apparatus == "Floor":
            self.season_avg_label.setText(f"Season Avg: {gymnast.floor_avg:.03f}")
        elif current_apparatus == "Vault":
            self.season_avg_label.setText(f"Season Avg: {gymnast.vault_avg:.03f}")
        else:
            self.apparatus_label.setText("No Apparatus")
            self.season_avg_label.setText("Season Avg: N/A")
        self.last_gymnast = gymnast

    def load_lineup_entry_information(self):
        lineup_entry: db.models.LineupEntry | None = self.event_lineup_manager.get_current_lineup_entry()
        if not lineup_entry:
            return

        self.order_label.setText(f"Order: {lineup_entry.order + 1}")
        self.score_label.setText(f"{lineup_entry.score:.03f}")

        if self.last_score != lineup_entry.score and lineup_entry.score != 0:
            self.flash_score()
        self.last_score = lineup_entry.score

    def refresh_ui(self):
        self.load_gymnast_information()
        self.load_lineup_entry_information()
        self.refresh_timer.start(100)

    def update_score_label(self, score):
        self.score_label.setText(score)
        self.flash_score()

    def flash_score(self):
        self.flash_timer.timeout.connect(self.toggle_color)
        self.flash_timer.start(500)

        self.stop_timer.timeout.connect(self.stop_flashing)
        self.stop_timer.start(3000)  # Stop flashing after 3 seconds

    def toggle_color(self):
        self.score_color_index = (self.score_color_index + 1) % 2
        if self.score_color_index:
            self.score_label.setStyleSheet("background-color: yellow; color: black")
        else:
            self.score_label.setStyleSheet("background-color: none; color: white")

    def stop_flashing(self):
        self.flash_timer.stop()
        self.stop_timer.stop()
        self.score_label.setStyleSheet("background-color: none; color: white")


class ArenaScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.db_interface = DBInterface.get_interface()
        self.meet_format = MeetData.get_data().meet_format

        self.quad_format = QGridLayout()
        self.quadrants = [TeamLayout(i) for i in range(self.meet_format)]
        for i, quadrant in enumerate(self.quadrants):
            self.quad_format.addLayout(quadrant, i % 2, (i // 2) % 2)
        self.setLayout(self.quad_format)


if __name__ == "__main__":
    print(os.listdir())
    db_interface = DBInterface.get_interface("../../db_setup/.env")

    meet_data = MeetData.get_data()
    meet_data.meet_format = 2
    meet_data.schools[0] = "University of Kentucky"
    meet_data.schools[1] = "The University of Alabama"
    app = QApplication(sys.argv)
    arena = ArenaScreen()
    arena.show()
    sys.exit(app.exec_())
