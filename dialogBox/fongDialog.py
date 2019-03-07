# -*- coding: utf-8 -*-

#   2019/3/7 0007 下午 1:53     

__author__ = 'RollingBear'

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lb1 = QLabel('KNOWLEDGE ONLY MATTERS', self)
        self.lb1.move(130, 20)

        vbox.addWidget(self.lb1)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font Dialog')

        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.lb1.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
