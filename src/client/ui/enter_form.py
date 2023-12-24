from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow
from client.API.User_api import get_login_password_user
from client.ui.db_search_viewing import Start_DB

main_window = None


class CustomMainWindowDB(QMainWindow, Start_DB):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def open_main_window_db():
    global main_window
    main_window = CustomMainWindowDB()
    main_window.show()


class EnterForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Enter Form')
        self.login_label = QLabel('Login:')
        self.login_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.enter_button = QPushButton('Enter')
        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.enter_button)
        self.setLayout(layout)
        self.enter_button.clicked.connect(self.enter)

    def enter(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if login and password:
            success = get_login_password_user(login, password)
            if success:
                print("Вы успешно вошли!")
                open_main_window_db()
            else:
                print("Данные введены неверно.")
        else:
            print("Введите логин и пароль.")

