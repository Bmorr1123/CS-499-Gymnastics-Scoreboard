import sys

from PyQt5.QtWidgets import (QApplication, QGridLayout, QPushButton, QWidget, QHBoxLayout, QLabel,)

import screensController

from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arena Screen")

        # create a QGridLayout instance (quad format)
        quadFormat = QGridLayout()

        # create a QGridLayout instance for each team
        team1 = QGridLayout()
        team2 = QGridLayout()
        team3 = QGridLayout()
        team4 = QGridLayout()

        # create a HBoxLayout instance for Images and Score
        imageScore1 = QHBoxLayout()
        imageScore2 = QHBoxLayout()
        imageScore3 = QHBoxLayout()
        imageScore4 = QHBoxLayout()
        # create score labels
        self.score1 = QLabel("0.00")
        self.score1.setFont(QFont('Arial', 50))
        self.score1.setAlignment(Qt.AlignCenter)
        self.score2 = QLabel("0.00")
        self.score2.setFont(QFont('Arial', 50))
        self.score2.setAlignment(Qt.AlignCenter)
        self.score3 = QLabel("0.00")
        self.score3.setFont(QFont('Arial', 50))
        self.score3.setAlignment(Qt.AlignCenter)
        self.score4 = QLabel("0.00")
        self.score4.setFont(QFont('Arial', 50))
        self.score4.setAlignment(Qt.AlignCenter)
        # create logo labels for teams
        if screensController.displayLogo:
            logo1 = QLabel()
            logo1.pixmap = QPixmap(screensController.competingSchools[0].school_logo)  # will need to transfer school logo in
            logo1.setPixmap(logo1.pixmap.scaled(150, 150))
            logo1.setAlignment(Qt.AlignCenter)
            imageScore1.addWidget(logo1, 1)
            logo2 = QLabel()
            logo2.pixmap = QPixmap(screensController.competingSchools[1].school_logo)  # will need to transfer school logo in
            logo2.setPixmap(logo1.pixmap.scaled(150, 150))
            logo2.setAlignment(Qt.AlignCenter)
            imageScore2.addWidget(logo2, 1)
            logo3 = QLabel()
            logo3.pixmap = QPixmap(screensController.competingSchools[2].school_logo)  # will need to transfer school logo in
            logo3.setPixmap(logo1.pixmap.scaled(150, 150))
            logo3.setAlignment(Qt.AlignCenter)
            imageScore3.addWidget(logo3, 1)
            logo4 = QLabel()
            logo4.pixmap = QPixmap(screensController.competingSchools[3].school_logo)  # will need to transfer school logo in
            logo4.setPixmap(logo1.pixmap.scaled(150, 150))
            logo4.setAlignment(Qt.AlignCenter)
            imageScore4.addWidget(logo4, 1)

        # create a VBoxLayout instance for gymnast info
        info1 = QVBoxLayout()
        info2 = QVBoxLayout()
        info3 = QVBoxLayout()
        info4 = QVBoxLayout()
        # create info for gymnast for teams


        # create info for gymnast for teams
        self.name1 = QLabel(screensController.name1s)
        self.name1.setFont(QFont('Arial', 20))
        self.class1 = QLabel(screensController.class1s)
        self.class1.setFont(QFont('Arial', 15))
        self.major1 = QLabel(screensController.major1s)
        self.major1.setFont(QFont('Arial', 15))
        self.avg1 = QLabel(screensController.avg1s)
        self.avg1.setFont(QFont('Arial', 15))
        self.name2 = QLabel(screensController.name2s)
        self.name2.setFont(QFont('Arial', 20))
        self.class2 = QLabel(screensController.class2s)
        self.class2.setFont(QFont('Arial', 15))
        self.major2 = QLabel(screensController.major2s)
        self.major2.setFont(QFont('Arial', 15))
        self.avg2 = QLabel(screensController.avg2s)
        self.avg2.setFont(QFont('Arial', 15))
        self.name3 = QLabel(screensController.name3s)
        self.name3.setFont(QFont('Arial', 20))
        self.class3 = QLabel(screensController.class3s)
        self.class3.setFont(QFont('Arial', 15))
        self.major3 = QLabel(screensController.major3s)
        self.major3.setFont(QFont('Arial', 15))
        self.avg3 = QLabel(screensController.avg3s)
        self.avg3.setFont(QFont('Arial', 15))
        self.name4 = QLabel(screensController.name4s)
        self.name4.setFont(QFont('Arial', 20))
        self.class4 = QLabel(screensController.class4s)
        self.class4.setFont(QFont('Arial', 15))
        self.major4 = QLabel(screensController.major4s)
        self.major4.setFont(QFont('Arial', 15))
        self.avg4 = QLabel(screensController.avg4s)
        self.avg4.setFont(QFont('Arial', 15))
        # create image labels for gymnasts
        image1 = QLabel()
        image1.pixmap = QPixmap('proPic.jpg')  # will need to transfer current gymnast pic in
        image1.setPixmap(image1.pixmap.scaled(150, 150))
        image1.setAlignment(Qt.AlignCenter)
        image2 = QLabel()
        image2.pixmap = QPixmap('proPic.jpg')  # will need to transfer current gymnast pic in
        image2.setPixmap(image1.pixmap.scaled(150, 150))
        image2.setAlignment(Qt.AlignCenter)
        image3 = QLabel()
        image3.pixmap = QPixmap('proPic.jpg')  # will need to transfer current gymnast pic in
        image3.setPixmap(image1.pixmap.scaled(150, 150))
        image3.setAlignment(Qt.AlignCenter)
        image4 = QLabel()
        image4.pixmap = QPixmap('proPic.jpg')  # will need to transfer current gymnast pic in
        image4.setPixmap(image1.pixmap.scaled(150, 150))
        image4.setAlignment(Qt.AlignCenter)
        # create order labels
        order1 = QLabel("Order: " + "1st")  # will need to be replaced with attribute
        order1.setFont(QFont('Arial', 30))
        order1.setAlignment(Qt.AlignCenter)
        order2 = QLabel("Order: " + "1st")  # will need to be replaced with attribute
        order2.setFont(QFont('Arial', 30))
        order2.setAlignment(Qt.AlignCenter)
        order3 = QLabel("Order: " + "1st")  # will need to be replaced with attribute
        order3.setFont(QFont('Arial', 30))
        order3.setAlignment(Qt.AlignCenter)
        order4 = QLabel("Order: " + "1st")  # will need to be replaced with attribute
        order4.setFont(QFont('Arial', 30))
        order4.setAlignment(Qt.AlignCenter)

        # create a HBoxLayout instance for event and start value
        event1 = QHBoxLayout()
        event2 = QHBoxLayout()
        event3 = QHBoxLayout()
        event4 = QHBoxLayout()
        # create apparatus labels
        app1 = QLabel("VT")
        app1.setFont(QFont('Arial', 20))
        app1.setAlignment(Qt.AlignCenter)
        app2 = QLabel("VT")
        app2.setFont(QFont('Arial', 20))
        app2.setAlignment(Qt.AlignCenter)
        app3 = QLabel("VT")
        app3.setFont(QFont('Arial', 20))
        app3.setAlignment(Qt.AlignCenter)
        app4 = QLabel("VT")
        app4.setFont(QFont('Arial', 20))
        app4.setAlignment(Qt.AlignCenter)
        # create start value labels
        if screensController.displaySV:
            sv1 = QLabel("SV")
            sv1.setFont(QFont('Arial', 20))
            sv1.setAlignment(Qt.AlignCenter)
            event1.addWidget(sv1)
            sv2 = QLabel("SV")
            sv2.setFont(QFont('Arial', 20))
            sv2.setAlignment(Qt.AlignCenter)
            event2.addWidget(sv2)
            sv3 = QLabel("SV")
            sv3.setFont(QFont('Arial', 20))
            sv3.setAlignment(Qt.AlignCenter)
            event3.addWidget(sv3)
            sv4 = QLabel("SV")
            sv4.setFont(QFont('Arial', 20))
            sv4.setAlignment(Qt.AlignCenter)
            event4.addWidget(sv4)

        # create vault name labels (only will display for vt event)
        vtName1 = QLabel("Vault Name")
        vtName1.setFont(QFont('Arial', 15))
        vtName2 = QLabel("Vault Name")
        vtName2.setFont(QFont('Arial', 15))
        vtName3 = QLabel("Vault Name")
        vtName3.setFont(QFont('Arial', 15))
        vtName4 = QLabel("Vault Name")
        vtName4.setFont(QFont('Arial', 15))

        # create a VBoxLayout instance for judges
        judges1 = QVBoxLayout()
        judges2 = QVBoxLayout()
        judges3 = QVBoxLayout()
        judges4 = QVBoxLayout()
        # create judge labels
        if screensController.displayJudges:
            judgeTitle1 = QLabel("Judges: ")
            judgeTitle1.setFont(QFont('Arial', 10))
            judge1Team1 = QLabel("Judge 1")
            judge1Team1.setFont(QFont('Arial', 10))
            judge2Team1 = QLabel("Judge 2")
            judge2Team1.setFont(QFont('Arial', 10))
            judge3Team1 = QLabel("Judge 3")
            judge3Team1.setFont(QFont('Arial', 10))
            judges1.addWidget(judgeTitle1)
            judges1.addWidget(judge1Team1)
            judges1.addWidget(judge2Team1)
            judges1.addWidget(judge3Team1)

            judgeTitle2 = QLabel("Judges: ")
            judgeTitle2.setFont(QFont('Arial', 10))
            judge1Team2 = QLabel("Judge 1")
            judge1Team2.setFont(QFont('Arial', 10))
            judge2Team2 = QLabel("Judge 2")
            judge2Team2.setFont(QFont('Arial', 10))
            judge3Team2 = QLabel("Judge 3")
            judge3Team2.setFont(QFont('Arial', 10))
            judges2.addWidget(judgeTitle2)
            judges2.addWidget(judge1Team2)
            judges2.addWidget(judge2Team2)
            judges2.addWidget(judge3Team2)

            judgeTitle3 = QLabel("Judges: ")
            judgeTitle3.setFont(QFont('Arial', 10))
            judge1Team3 = QLabel("Judge 1")
            judge1Team3.setFont(QFont('Arial', 10))
            judge2Team3 = QLabel("Judge 2")
            judge2Team3.setFont(QFont('Arial', 10))
            judge3Team3 = QLabel("Judge 3")
            judge3Team3.setFont(QFont('Arial', 10))
            judges3.addWidget(judgeTitle3)
            judges3.addWidget(judge1Team3)
            judges3.addWidget(judge2Team3)
            judges3.addWidget(judge3Team3)

            judgeTitle4 = QLabel("Judges: ")
            judgeTitle4.setFont(QFont('Arial', 10))
            judge1Team4 = QLabel("Judge 1")
            judge1Team4.setFont(QFont('Arial', 10))
            judge2Team4 = QLabel("Judge 2")
            judge2Team4.setFont(QFont('Arial', 10))
            judge3Team4 = QLabel("Judge 3")
            judge3Team4.setFont(QFont('Arial', 10))
            judges4.addWidget(judgeTitle4)
            judges4.addWidget(judge1Team4)
            judges4.addWidget(judge2Team4)
            judges4.addWidget(judge3Team4)

        # create timer labels
        timer1 = QLabel("--:--")
        timer1.setFont(QFont('Arial', 40))
        timer1.setAlignment(Qt.AlignCenter)
        timer2 = QLabel("--:--")
        timer2.setFont(QFont('Arial', 40))
        timer2.setAlignment(Qt.AlignCenter)
        timer3 = QLabel("--:--")
        timer3.setFont(QFont('Arial', 40))
        timer3.setAlignment(Qt.AlignCenter)
        timer4 = QLabel("--:--")
        timer4.setFont(QFont('Arial', 40))
        timer4.setAlignment(Qt.AlignCenter)

        # add team layouts to quad format
        quadFormat.addLayout(team1, 0, 0)
        quadFormat.addLayout(team2, 0, 1)
        quadFormat.addLayout(team3, 1, 0)
        quadFormat.addLayout(team4, 1, 1)

        # add widgets to inner layouts
        # ~team 1~
        team1.addLayout(imageScore1, 0, 0, 1, 3)
        imageScore1.addWidget(self.score1, 2)

        team1.addLayout(info1, 1, 0, 1, 1)
        info1.addWidget(self.name1)
        info1.addWidget(self.class1)
        info1.addWidget(self.major1)
        info1.addWidget(self.avg1)
        team1.addWidget(image1, 1, 1)

        if screensController.displayOrder:
            team1.addWidget(order1, 1, 2)

        team1.addLayout(event1, 2, 0, 1, 2)
        event1.addWidget(app1)

        team1.addWidget(vtName1, 3, 0, 1, 2)

        team1.addLayout(judges1, 2, 2, 2, 1)

        team1.addWidget(timer1, 4, 0, 1, 3)

        # ~team 2~
        team2.addLayout(imageScore2, 0, 0, 1, 3)
        imageScore2.addWidget(self.score2, 2)

        team2.addLayout(info2, 1, 0, 1, 1)
        info2.addWidget(self.name2)
        info2.addWidget(self.class2)
        info2.addWidget(self.major2)
        info2.addWidget(self.avg2)
        team2.addWidget(image2, 1, 1)

        if screensController.displayOrder:
            team2.addWidget(order2, 1, 2)

        team2.addLayout(event2, 2, 0, 1, 2)
        event2.addWidget(app2)

        team2.addWidget(vtName2, 3, 0, 1, 2)

        team2.addLayout(judges2, 2, 2, 2, 1)

        team2.addWidget(timer2, 4, 0, 1, 3)

        # ~team 3~
        if screensController.meetFormat == "Tri" or screensController.meetFormat == "Quad":
            team3.addLayout(imageScore3, 0, 0, 1, 3)
            imageScore3.addWidget(self.score3, 2)

            team3.addLayout(info3, 1, 0, 1, 1)
            info3.addWidget(self.name3)
            info3.addWidget(self.class3)
            info3.addWidget(self.major3)
            info3.addWidget(self.avg3)
            team3.addWidget(image3, 1, 1)

            if screensController.displayOrder:
                team3.addWidget(order3, 1, 2)

            team3.addLayout(event3, 2, 0, 1, 2)
            event3.addWidget(app3)

            team3.addWidget(vtName3, 3, 0, 1, 2)

            team3.addLayout(judges3, 2, 2, 2, 1)

            team3.addWidget(timer3, 4, 0, 1, 3)

        # ~team 4~
        if screensController.meetFormat == "Quad":
            team4.addLayout(imageScore4, 0, 0, 1, 3)
            imageScore4.addWidget(self.score4, 2)

            team4.addLayout(info4, 1, 0, 1, 1)
            info4.addWidget(self.name4)
            info4.addWidget(self.class4)
            info4.addWidget(self.major4)
            info4.addWidget(self.avg4)
            team4.addWidget(image4, 1, 1)

            if screensController.displayOrder:
                team4.addWidget(order4, 1, 2)

            team4.addLayout(event4, 2, 0, 1, 2)
            event4.addWidget(app4)

            team4.addWidget(vtName4, 3, 0, 1, 2)

            team4.addLayout(judges4, 2, 2, 2, 1)

            team4.addWidget(timer4, 4, 0, 1, 3)

        # set the layout on the application's window
        self.setLayout(quadFormat)

    def update_gymnast1(self, name, classification, major, average):
        self.name1.setText(name)
        self.class1.setText(classification)
        self.major1.setText(major)
        self.avg1.setText(average)

    def update_gymnast2(self, name, classification, major, average):
        self.name2.setText(name)
        self.class2.setText(classification)
        self.major2.setText(major)
        self.avg2.setText(average)

    def update_gymnast3(self, name, classification, major, average):
        self.name3.setText(name)
        self.class3.setText(classification)
        self.major3.setText(major)
        self.avg3.setText(average)

    def update_gymnast4(self, name, classification, major, average):
        self.name4.setText(name)
        self.class4.setText(classification)
        self.major4.setText(major)
        self.avg4.setText(average)

    def update_scoreLabel1(self, score):
        self.score1.setText(score)
        self.flash_score(1)

    def update_scoreLabel2(self, score):
        self.score2.setText(score)
        self.flash_score(2)

    def update_scoreLabel3(self, score):
        self.score3.setText(score)
        self.flash_score(3)

    def update_scoreLabel4(self, score):
        self.score4.setText(score)
        self.flash_score(4)

    def flash_score(self, team):
        if team == 1:
            self.flash_timer1 = QTimer(self)
            self.flash_timer1.timeout.connect(self.toggle_color1)
            self.flash_timer1.start(500)

            self.stop_timer1 = QTimer(self)
            self.stop_timer1.timeout.connect(self.stop_flashing1)
            self.stop_timer1.start(3000)  # Stop flashing after 3 seconds
        elif team == 2:
            self.flash_timer2 = QTimer(self)
            self.flash_timer2.timeout.connect(self.toggle_color2)
            self.flash_timer2.start(500)

            self.stop_timer2 = QTimer(self)
            self.stop_timer2.timeout.connect(self.stop_flashing2)
            self.stop_timer2.start(3000)  # Stop flashing after 3 seconds
        elif team == 3:
            self.flash_timer3 = QTimer(self)
            self.flash_timer3.timeout.connect(self.toggle_color3)
            self.flash_timer3.start(500)

            self.stop_timer3 = QTimer(self)
            self.stop_timer3.timeout.connect(self.stop_flashing3)
            self.stop_timer3.start(3000)  # Stop flashing after 3 seconds
        elif team == 4:
            self.flash_timer4 = QTimer(self)
            self.flash_timer4.timeout.connect(self.toggle_color4)
            self.flash_timer4.start(500)

            self.stop_timer4 = QTimer(self)
            self.stop_timer4.timeout.connect(self.stop_flashing4)
            self.stop_timer4.start(3000)  # Stop flashing after 3 seconds

    def toggle_color1(self):
        palette = self.score1.palette()
        color = palette.color(self.score1.foregroundRole())
        if color == QColor("black"):
            self.score1.setStyleSheet("background-color: yellow; color: white")
        else:
            self.score1.setStyleSheet("background-color: none; color: black")

    def toggle_color2(self):
        palette = self.score2.palette()
        color = palette.color(self.score2.foregroundRole())
        if color == QColor("black"):
            self.score2.setStyleSheet("background-color: yellow; color: white")
        else:
            self.score2.setStyleSheet("background-color: none; color: black")

    def toggle_color3(self):
        palette = self.score3.palette()
        color = palette.color(self.score3.foregroundRole())
        if color == QColor("black"):
            self.score3.setStyleSheet("background-color: yellow; color: white")
        else:
            self.score3.setStyleSheet("background-color: none; color: black")

    def toggle_color4(self):
        palette = self.score4.palette()
        color = palette.color(self.score4.foregroundRole())
        if color == QColor("black"):
            self.score4.setStyleSheet("background-color: yellow; color: white")
        else:
            self.score4.setStyleSheet("background-color: none; color: black")

    def stop_flashing1(self):
        self.flash_timer1.stop()
        self.stop_timer1.stop()
        self.score1.setStyleSheet("background-color: none; color: black")

    def stop_flashing2(self):
        self.flash_timer2.stop()
        self.stop_timer2.stop()
        self.score2.setStyleSheet("background-color: none; color: black")

    def stop_flashing3(self):
        self.flash_timer3.stop()
        self.stop_timer3.stop()
        self.score3.setStyleSheet("background-color: none; color: black")

    def stop_flashing4(self):
        self.flash_timer4.stop()
        self.stop_timer4.stop()
        self.score4.setStyleSheet("background-color: none; color: black")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    arena = Window()
    arena.show()
    sys.exit(app.exec_())
