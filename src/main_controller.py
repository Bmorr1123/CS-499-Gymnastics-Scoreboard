from PyQt5.QtCore import QEventLoop
from PyQt5.QtWidgets import QApplication

from db_interface import DBInterface
import sys, ui



def main():
    database_interface = DBInterface.get_interface("../db_setup/.env")

    app = QApplication(sys.argv)

    loop = QEventLoop()

    setup_screen = ui.SetupScreen()
    setup_screen.show()
    setup_screen.destroyed.connect(loop.quit)
    # arena_screen = ui.ArenaScreen(database_interface)
    # post_screen = ui.PostScreen(database_interface)

    sys.exit(app.exec_())




    main_controller = MainController(database_interface)


if __name__ == "__main__":
    main()