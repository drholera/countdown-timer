from countdown_timer.ui.design import Ui_MainWindow
from countdown_timer.utils.time_converter import TimeConverter
from PyQt5 import QtWidgets, QtCore
import sys


class CountdownTimer(QtWidgets.QMainWindow):
    __seconds = 0

    intervals = (
        ('weeks', 604800),  # 60 * 60 * 24 * 7
        ('days', 86400),  # 60 * 60 * 24
        ('hours', 3600),  # 60 * 60
        ('minutes', 60),
        ('seconds', 1),
    )

    def __init__(self):
        super(CountdownTimer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setText('Please enter time to countdown. Format - HH:MM:SS')
        self.ui.label.setGeometry(QtCore.QRect(130, 60, 551, 21))

        self.ui.pushButton.clicked.connect(self.clickStart)

    def clickStart(self):
        countdown_time = self.ui.lineEdit.text()
        if countdown_time is None or not TimeConverter().validate_input_time(countdown_time):
            self.ui.label.setText('Please enter VALID time to countdown. Format - HH:MM:SS')
            return

        self.__seconds = TimeConverter().get_seconds(countdown_time)
        self.ui.lcdNumber.display(countdown_time)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = CountdownTimer()
    application.show()

    sys.exit(app.exec())
