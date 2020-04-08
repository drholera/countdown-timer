
from countdown_timer.ui.design import Ui_MainWindow
from countdown_timer.utils.time_converter import TimeConverter
from PyQt5 import QtWidgets, QtCore
import sys


class CountdownTimer(QtWidgets.QMainWindow):
    __seconds = 0
    __time_converter = TimeConverter()
    __t = QtCore.QTimer()

    def __init__(self):
        super(CountdownTimer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setText('Please enter time to countdown. Format - HH:MM:SS')
        self.ui.label.setGeometry(QtCore.QRect(130, 60, 551, 21))

        self.ui.lcdNumber.setDigitCount(8)
        self.ui.lcdNumber.setGeometry(QtCore.QRect(130, 90, 600, 80))

        self.ui.pushButton.clicked.connect(self.click_start)

    def click_start(self):
        if self.__t.isActive():
            self.__t.stop()

        countdown_time = self.ui.lineEdit.text()
        if countdown_time is None or not TimeConverter().validate_input_time(countdown_time):
            self.ui.label.setText('Please enter VALID time to countdown. Format - HH:MM:SS')
            return

        self.__seconds = self.__time_converter.time_to_seconds(countdown_time)
        self.ui.lcdNumber.display(countdown_time)

        def run_timer():
            """Tricky point, to avoid freezing of the app during countdown."""
            if self.__seconds >= 0:
                rt = self.__time_converter.seconds_to_time(self.__seconds)
                self.ui.lcdNumber.display(rt)
                self.__seconds -= 1
            else:
                self.__t.stop()

        self.__t.timeout.connect(run_timer)
        self.__t.setInterval(1000)
        self.__t.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = CountdownTimer()
    application.show()

    sys.exit(app.exec())
