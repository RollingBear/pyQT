# -*- coding: utf-8 -*-

#   2019/3/4 0004 下午 3:34     

__author__ = 'RollingBear'

import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        # need a icon as png
        self.setWindowIcon('web.png')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
