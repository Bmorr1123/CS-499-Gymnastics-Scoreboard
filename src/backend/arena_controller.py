from db_interface import DBInterface


class ArenaController:
    def __init__(self, database_interface: DBInterface):
        self.database_interface = database_interface
