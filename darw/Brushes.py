# -*- coding: utf-8 -*-

#   2019/3/13 0013 上午 10:00     

__author__ = 'RollingBear'


import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()


    def drawBrushes(self, QPainter):

        brush = QBrush(Qt.SolidPattern)
        QPainter.setBrush(brush)
        QPainter.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        QPainter.setBrush(brush)
        QPainter.drawRect(130, 15, 90, 60)

        brush.setStyle(Qt.Dense2Pattern)
        QPainter.setBrush(brush)
        QPainter.drawRect(250, 15, 90, 60)

        brush.setStyle(Qt.DiagCrossPattern)
        QPainter.setBrush(brush)
        QPainter.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.Dense5Pattern)
        QPainter.setBrush(brush)
        QPainter.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        QPainter.setBrush(brush)
        QPainter.drawRect(250, 105, 90, 60)

        brush.setStyle(Qt.HorPattern)
        QPainter.setBrush(brush)
        QPainter.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerPattern)
        QPainter.setBrush(brush)
        QPainter.drawRect(130, 195, 90, 60)

        brush.setStyle(Qt.BDiagPattern)
        QPainter.setBrush(brush)
        QPainter.drawRect(250, 195, 90, 60)


    def paintEvent(self, QPaintEvent):

        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())