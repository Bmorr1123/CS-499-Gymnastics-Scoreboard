import sys

from PyQt5.QtWidgets import QApplication

import setupScreen
import scorekeeperScreen
import arenaScreen


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = setupScreen.Window()
    window.show()
    sys.exit(app.exec_())

