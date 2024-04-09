import updateLineup

global uScreen


def open_window():
    global uScreen
    uScreen = updateLineup.Window()
    uScreen.show()


def close_window():
    uScreen.close()

