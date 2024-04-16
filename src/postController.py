import postScreen
import screensController

global pScreen
global sortedScores


def open_window():
    final_placements()

    global pScreen
    pScreen = postScreen.Window()
    pScreen.show()


def close_window():
    pScreen.close()


def final_placements():
    finalScores = [screensController.meetScores1, screensController.meetScores2, screensController.meetScores3,
                   screensController.meetScores4]
    global sortedScores
    sortedScores = sorted(finalScores, reverse=True)
