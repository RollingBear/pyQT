# -*- coding: utf-8 -*-

#   2019/3/7 0007 上午 10:35     

__author__ = 'RollingBear'

import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        color = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % color.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color Dialog')

        self.show()

    def showDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % color.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
