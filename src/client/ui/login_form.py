import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from client.API.User_api import get_login_user, post_user


class RegistrationForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registration Form')
        self.login_label = QLabel('Login:')
        self.login_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.register_button = QPushButton('Register')
        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)
        self.setLayout(layout)
        self.register_button.clicked.connect(self.register)

    def create_user(self, login, password):
        response = post_user(login, password)
        if response.status_code == 200:
            return True
        else:
            print(f"Ошибка при создании пользователя. Код ошибки: {response.status_code}")
            return False

    def register(self):
        login = self.login_input.text()
        password = self.password_input.text()
        if login and password:
            existing_user = get_login_user(login)
            if not existing_user:
                success = self.create_user(login, password)
                if success:
                    print("Пользователь зарегистрирован успешно!")
                else:
                    print("Не удалось создать пользователя.")
            else:
                print("Пользователь с таким логином уже существует.")
        else:
            print("Введите логин и пароль.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RegistrationForm()
    form.setWindowFlag(Qt.WindowCloseButtonHint)
    form.show()
    sys.exit(app.exec_())
