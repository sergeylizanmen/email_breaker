from PyQt6 import QtWidgets
import interface_breaker


class EmailBreaker(QtWidgets.QMainWindow, interface_breaker.Ui_MainWindow):
    def __init__(self):
        """
        Инициализация экземпляра класса

        Создается интерфейс по файлу 'interface_breaker.py'
        Указывается, какие функции должны выполнять кнопки
        """
        super().__init__()
        self.setupUi(self)

        self.ButtonGo.clicked.connect(self.go)
        self.ButtonCopy_login.clicked.connect(self.copy_login)
        self.ButtonCopy_domain.clicked.connect(self.copy_domain)

    def go(self):
        """
        Функция для кнопки 'Go'

        Проверяет правильность имейла, затем делит его
        Если ловится исключение, то ничего не происходит
        """
        email = self.lineGo.text()
        try:
            login, domain = email.split('@')
            if login == '' or domain == '':
                raise ValueError
            if '.' not in domain:
                raise ValueError

            self.lineLogin.setText(login)
            self.lineDomain.setText(domain)
            self.lineGo.clear()
            self.lineGo.setPlaceholderText('')
        except Exception:
            pass

    """ Две функции для кнопок копирования """
    def copy_login(self):
        self.clipboard = QtWidgets.QApplication.clipboard()
        self.clipboard.setText(self.lineLogin.text())

    def copy_domain(self):
        self.clipboard = QtWidgets.QApplication.clipboard()
        self.clipboard.setText(self.lineDomain.text())


app = QtWidgets.QApplication([])
window = EmailBreaker()
window.show()
app.exec()
