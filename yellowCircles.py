import sys

from PyQt5.QtGui import QPainter, QColor
import random

from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets, uic


class Drawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellowCircles.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.need_paint = False

    def paint(self):
        self.need_paint = True
        self.update()

    def draw_me(self, qp):
        qp.setBrush(QColor(255, 215, 0))
        radius = random.randint(10, 90)
        qp.drawEllipse(0, 0, radius, radius)

    def paintEvent(self, event):
        if not self.need_paint:
            return
        qp = QPainter()
        qp.begin(self)
        self.draw_me(qp)
        self.need_paint = False
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Drawer()
    ex.show()
    sys.exit(app.exec_())
