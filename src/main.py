import sys

from PyQt5.QtWidgets import QApplication

import setupController


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupController.open_window()
    sys.exit(app.exec_())

