import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget, QHBoxLayout, QLabel,
)

from PyQt5.QtCore import Qt

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


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
        score1 = QLabel("180.99")
        score1.setFont(QFont('Arial', 50))
        score1.setAlignment(Qt.AlignCenter)
        score2 = QLabel("180.99")
        score2.setFont(QFont('Arial', 50))
        score2.setAlignment(Qt.AlignCenter)
        score3 = QLabel("180.99")
        score3.setFont(QFont('Arial', 50))
        score3.setAlignment(Qt.AlignCenter)
        score4 = QLabel("180.99")
        score4.setFont(QFont('Arial', 50))
        score4.setAlignment(Qt.AlignCenter)
        # create logo labels for teams
        logo1 = QLabel()
        logo1.pixmap = QPixmap('exampleLogo.jpg')  # will need to transfer school logo in
        logo1.setPixmap(logo1.pixmap.scaled(150, 150))
        logo1.setAlignment(Qt.AlignCenter)
        logo2 = QLabel()
        logo2.pixmap = QPixmap('exampleLogo.jpg')  # will need to transfer school logo in
        logo2.setPixmap(logo1.pixmap.scaled(150, 150))
        logo2.setAlignment(Qt.AlignCenter)
        logo3 = QLabel()
        logo3.pixmap = QPixmap('exampleLogo.jpg')  # will need to transfer school logo in
        logo3.setPixmap(logo1.pixmap.scaled(150, 150))
        logo3.setAlignment(Qt.AlignCenter)
        logo4 = QLabel()
        logo4.pixmap = QPixmap('exampleLogo.jpg')  # will need to transfer school logo in
        logo4.setPixmap(logo1.pixmap.scaled(150, 150))
        logo4.setAlignment(Qt.AlignCenter)

        # create a VBoxLayout instance for gymnast info
        info1 = QVBoxLayout()
        info2 = QVBoxLayout()
        info3 = QVBoxLayout()
        info4 = QVBoxLayout()
        # create info for gymnast for teams
        name1 = QLabel("Name")
        name1.setFont(QFont('Arial', 25))
        class1 = QLabel("Classification")
        class1.setFont(QFont('Arial', 15))
        major1 = QLabel("Major")
        major1.setFont(QFont('Arial', 15))
        avg1 = QLabel("Season Average")
        avg1.setFont(QFont('Arial', 15))
        name2 = QLabel("Name")
        name2.setFont(QFont('Arial', 25))
        class2 = QLabel("Classification")
        class2.setFont(QFont('Arial', 15))
        major2 = QLabel("Major")
        major2.setFont(QFont('Arial', 15))
        avg2 = QLabel("Season Average")
        avg2.setFont(QFont('Arial', 15))
        name3 = QLabel("Name")
        name3.setFont(QFont('Arial', 25))
        class3 = QLabel("Classification")
        class3.setFont(QFont('Arial', 15))
        major3 = QLabel("Major")
        major3.setFont(QFont('Arial', 15))
        avg3 = QLabel("Season Average")
        avg3.setFont(QFont('Arial', 15))
        name4 = QLabel("Name")
        name4.setFont(QFont('Arial', 25))
        class4 = QLabel("Classification")
        class4.setFont(QFont('Arial', 15))
        major4 = QLabel("Major")
        major4.setFont(QFont('Arial', 15))
        avg4 = QLabel("Season Average")
        avg4.setFont(QFont('Arial', 15))
        # create image labels for gymnasts
        image1 = QLabel()
        image1.pixmap = QPixmap('proPic.jpg')  # will need to transfer current gymnast pic in
        image1.setPixmap(image1.pixmap.scaled(200, 200))
        image1.setAlignment(Qt.AlignCenter)
        image2 = QLabel()
        image2.pixmap = QPixmap('proPic.jpg')  # will need to transfer current gymnast pic in
        image2.setPixmap(image1.pixmap.scaled(200, 200))
        image2.setAlignment(Qt.AlignCenter)
        image3 = QLabel()
        image3.pixmap = QPixmap('proPic.jpg')  # will need to transfer current gymnast pic in
        image3.setPixmap(image1.pixmap.scaled(200, 200))
        image3.setAlignment(Qt.AlignCenter)
        image4 = QLabel()
        image4.pixmap = QPixmap('proPic.jpg')  # will need to transfer current gymnast pic in
        image4.setPixmap(image1.pixmap.scaled(200, 200))
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
        sv1 = QLabel("SV")
        sv1.setFont(QFont('Arial', 20))
        sv1.setAlignment(Qt.AlignCenter)
        sv2 = QLabel("SV")
        sv2.setFont(QFont('Arial', 20))
        sv2.setAlignment(Qt.AlignCenter)
        sv3 = QLabel("SV")
        sv3.setFont(QFont('Arial', 20))
        sv3.setAlignment(Qt.AlignCenter)
        sv4 = QLabel("SV")
        sv4.setFont(QFont('Arial', 20))
        sv4.setAlignment(Qt.AlignCenter)

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
        judgeTitle1 = QLabel("Judges: ")
        judgeTitle1.setFont(QFont('Arial', 10))
        judge1Team1 = QLabel("Judge 1")
        judge1Team1.setFont(QFont('Arial', 10))
        judge2Team1 = QLabel("Judge 2")
        judge2Team1.setFont(QFont('Arial', 10))
        judge3Team1 = QLabel("Judge 3")
        judge3Team1.setFont(QFont('Arial', 10))
        judgeTitle2 = QLabel("Judges: ")
        judgeTitle2.setFont(QFont('Arial', 10))
        judge1Team2 = QLabel("Judge 1")
        judge1Team2.setFont(QFont('Arial', 10))
        judge2Team2 = QLabel("Judge 2")
        judge2Team2.setFont(QFont('Arial', 10))
        judge3Team2 = QLabel("Judge 3")
        judge3Team2.setFont(QFont('Arial', 10))
        judgeTitle3 = QLabel("Judges: ")
        judgeTitle3.setFont(QFont('Arial', 10))
        judge1Team3 = QLabel("Judge 1")
        judge1Team3.setFont(QFont('Arial', 10))
        judge2Team3 = QLabel("Judge 2")
        judge2Team3.setFont(QFont('Arial', 10))
        judge3Team3 = QLabel("Judge 3")
        judge3Team3.setFont(QFont('Arial', 10))
        judgeTitle4 = QLabel("Judges: ")
        judgeTitle4.setFont(QFont('Arial', 10))
        judge1Team4 = QLabel("Judge 1")
        judge1Team4.setFont(QFont('Arial', 10))
        judge2Team4 = QLabel("Judge 2")
        judge2Team4.setFont(QFont('Arial', 10))
        judge3Team4 = QLabel("Judge 3")
        judge3Team4.setFont(QFont('Arial', 10))

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
        imageScore1.addWidget(logo1, 1)
        imageScore1.addWidget(score1, 2)

        team1.addLayout(info1, 1, 0, 1, 1)
        info1.addWidget(name1)
        info1.addWidget(class1)
        info1.addWidget(major1)
        info1.addWidget(avg1)
        team1.addWidget(image1, 1, 1)
        team1.addWidget(order1, 1, 2)

        team1.addLayout(event1, 2, 0, 1, 2)
        event1.addWidget(app1)
        event1.addWidget(sv1)

        team1.addWidget(vtName1, 3, 0, 1, 2)

        team1.addLayout(judges1, 2, 2, 2, 1)
        judges1.addWidget(judgeTitle1)
        judges1.addWidget(judge1Team1)
        judges1.addWidget(judge2Team1)
        judges1.addWidget(judge3Team1)

        team1.addWidget(timer1, 4, 0, 1, 3)

        # ~team 2~
        team2.addLayout(imageScore2, 0, 0, 1, 3)
        imageScore2.addWidget(logo2, 1)
        imageScore2.addWidget(score2, 2)

        team2.addLayout(info2, 1, 0, 1, 1)
        info2.addWidget(name2)
        info2.addWidget(class2)
        info2.addWidget(major2)
        info2.addWidget(avg2)
        team2.addWidget(image2, 1, 1)
        team2.addWidget(order2, 1, 2)

        team2.addLayout(event2, 2, 0, 1, 2)
        event2.addWidget(app2)
        event2.addWidget(sv2)

        team2.addWidget(vtName2, 3, 0, 1, 2)

        team2.addLayout(judges2, 2, 2, 2, 1)
        judges2.addWidget(judgeTitle2)
        judges2.addWidget(judge1Team2)
        judges2.addWidget(judge2Team2)
        judges2.addWidget(judge3Team2)

        team2.addWidget(timer2, 4, 0, 1, 3)

        # ~team 3~
        if True:  # change this and team 4 to "false" to see dual meet format
            team3.addLayout(imageScore3, 0, 0, 1, 3)
            imageScore3.addWidget(logo3, 1)
            imageScore3.addWidget(score3, 2)

            team3.addLayout(info3, 1, 0, 1, 1)
            info3.addWidget(name3)
            info3.addWidget(class3)
            info3.addWidget(major3)
            info3.addWidget(avg3)
            team3.addWidget(image3, 1, 1)
            team3.addWidget(order3, 1, 2)

            team3.addLayout(event3, 2, 0, 1, 2)
            event3.addWidget(app3)
            event3.addWidget(sv3)

            team3.addWidget(vtName3, 3, 0, 1, 2)

            team3.addLayout(judges3, 2, 2, 2, 1)
            judges3.addWidget(judgeTitle3)
            judges3.addWidget(judge1Team3)
            judges3.addWidget(judge2Team3)
            judges3.addWidget(judge3Team3)

            team3.addWidget(timer3, 4, 0, 1, 3)

        # ~team 4~
        if True:  # change this to "false" to see triangular meet format
            team4.addLayout(imageScore4, 0, 0, 1, 3)
            imageScore4.addWidget(logo4, 1)
            imageScore4.addWidget(score4, 2)

            team4.addLayout(info4, 1, 0, 1, 1)
            info4.addWidget(name4)
            info4.addWidget(class4)
            info4.addWidget(major4)
            info4.addWidget(avg4)
            team4.addWidget(image4, 1, 1)
            team4.addWidget(order4, 1, 2)

            team4.addLayout(event4, 2, 0, 1, 2)
            event4.addWidget(app4)
            event4.addWidget(sv4)

            team4.addWidget(vtName4, 3, 0, 1, 2)

            team4.addLayout(judges4, 2, 2, 2, 1)
            judges4.addWidget(judgeTitle4)
            judges4.addWidget(judge1Team4)
            judges4.addWidget(judge2Team4)
            judges4.addWidget(judge3Team4)

            team4.addWidget(timer4, 4, 0, 1, 3)

        # set the layout on the application's window
        self.setLayout(quadFormat)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
