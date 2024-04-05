import postScreen

global pScreen


def open_window():
    global pScreen
    pScreen = postScreen.Window()
    pScreen.show()


def close_window():
    pScreen.close()
