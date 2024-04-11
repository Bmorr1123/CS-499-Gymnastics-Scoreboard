import setupScreen

global setScreen


def open_window():
    global setScreen
    setScreen = setupScreen.Window()
    setScreen.show()


def close_window():
    setScreen.close()
