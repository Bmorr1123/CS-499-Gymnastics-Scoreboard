from db_interface import DBInterface


class PostController:
    def __init__(self, database_interface: DBInterface):
        self.database_interface = database_interface