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
