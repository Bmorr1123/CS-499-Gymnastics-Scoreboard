import setupScreen
from src.db.db_interface import DBInterface

global setScreen

db_int = DBInterface("../db_setup/.env")


def open_window():
    global setScreen
    setScreen = setupScreen.Window()
    setScreen.show()


def close_window():
    setScreen.close()
