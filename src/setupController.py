import setupScreen
from db_interface import DBInterface

global setScreen

schools_selected = []

db_int = DBInterface.get_interface("../db_setup/.env")


def open_window():
    global setScreen
    setScreen = setupScreen.Window()
    setScreen.show()


def close_window():
    setScreen.close()
