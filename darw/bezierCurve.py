# -*- coding: utf-8 -*-

#   2019/3/13 0013 下午 4:31     

__author__ = 'RollingBear'

import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Bezier Curve')

        self.show()

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()

    def drawBezierCurve(self, QPainter):
        path = QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 20, 200, 350, 350, 30)

        QPainter.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
