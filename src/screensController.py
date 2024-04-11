import arenaScreen
import scorekeeperScreen

global aScreen
global sScreen


def open_windows():
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
