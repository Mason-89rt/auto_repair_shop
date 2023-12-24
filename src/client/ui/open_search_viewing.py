from PyQt5.QtWidgets import QMainWindow
from client.ui.viewing_tables_db import WindowDB
from client.ui.search_tables_main import search

main_window = None

def open_main_window(window_class):
    global main_window
    main_window = window_class()
    main_window.show()


class Search(QMainWindow, search):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Viewing(QMainWindow, WindowDB):
    def __init__(self):
        super().__init__()
        self.setupUi(self)





