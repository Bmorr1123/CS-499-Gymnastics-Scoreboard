from db_interface import DBInterface
from ui import SetupScreen


class SetupController:
    def __init__(self, database_interface: DBInterface):
        self.database_interface = database_interface

        print("Initing SetupScreen")
        self.setup_screen = ()
        print("Finished Initing SetupScreen")
        self.setup_screen.show()
        print("Finished Showing")

