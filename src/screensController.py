import arenaScreen
import scorekeeperScreen

global aScreen
global sScreen
global displayLogo
global displayOrder
global displaySV
global displayJudges
global meetFormat


def open_windows(check1, check2, check3, check4, format):
    global displayLogo
    displayLogo = check1

    global displayOrder
    displayOrder = check2

    global displaySV
    displaySV = check3

    global displayJudges
    displayJudges = check4

    global meetFormat
    meetFormat = format

    global aScreen
    aScreen = arenaScreen.Window()
    aScreen.show()
    global sScreen
    sScreen = scorekeeperScreen.Window()
    sScreen.show()


def close_windows():
    aScreen.close()
    sScreen.close()


def update_score(team, score):
    if team == 1:
        arenaScreen.Window.update_scoreLabel1(aScreen, score)
    if team == 2:
        arenaScreen.Window.update_scoreLabel2(aScreen, score)
    if team == 3:
        arenaScreen.Window.update_scoreLabel3(aScreen, score)
    if team == 4:
        arenaScreen.Window.update_scoreLabel4(aScreen, score)
