# -*- coding: utf-8 -*-

#   2019/3/4 0004 下午 2:37     

__author__ = 'RollingBear'


import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())