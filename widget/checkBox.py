# -*- coding: utf-8 -*-

#   2019/3/13 0013 下午 4:58     

__author__ = 'RollingBear'

import sys

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        checkBox = QCheckBox('show title', self)
        checkBox.move(20, 20)
        checkBox.toggle()
        checkBox.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')

        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
