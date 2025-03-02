"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


from PySide6 import QtWidgets, QtCore
from ui.c_signals_events_form import Ui_Form
import sys


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.w_screen, self.h_screen = QtWidgets.QApplication.primaryScreen().availableGeometry().size().toTuple()  ##получили ширину и высоту
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()


    def initSignals(self):
        self.ui.pushButtonGetData.clicked.connect(self.get_window_data)
        self.ui.pushButtonMoveCoords.clicked.connect(self.move_to_coord)
        self.ui.pushButtonLT.clicked.connect(lambda: self.move(0, 0))
        self.ui.pushButtonRT.clicked.connect(lambda: self.move(self.w_screen - self.width(), 0))
        self.ui.pushButtonLB.clicked.connect(lambda: self.move(0, self.h_screen-self.height()))
        self.ui.pushButtonRB.clicked.connect(lambda: self.move(self.w_screen - self.width(), self.h_screen - self.height()))
        self.ui.pushButtonCenter.clicked.connect(lambda: self.move(self.w_screen // 2 - self.width() // 2, self.h_screen // 2 - self.height() // 2))





    def get_window_data(self):
        app = QtWidgets.QApplication
        screen_count = len(app.screens())
        current_screen = app.primaryScreen().name()
        screen_res = app.primaryScreen().size()
        win_size = self.size()
        min_win_size = self.minimumSize()
        win_pos = self.pos()
        win_center = self.rect().center()
        win_state = self.windowState()


        data = f"""
        Кол-во экранов: {screen_count}
        Текущее основное окно: {current_screen}
        Разрешение экрана: {screen_res}
        На каком экране окно находится: {self.screen().name()}
        Размеры окна: {win_size}
        Минимальные размеры окна: {min_win_size}
        Текущее положение (координаты) окна: {win_pos}
        Координаты центра приложения: {win_center}
        Отслеживание состояния окна: {win_state}
        
        """

        self.ui.plainTextEdit.appendPlainText(data)

    def move_to_coord(self):
        x, y = self.ui.spinBoxX.value(), self.ui.spinBoxY.value()
        self.move(x, y)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
