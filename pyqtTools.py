# -*- coding: utf-8 -*-

#   2019/3/4 0004 下午 5:26     

__author__ = 'RollingBear'

'''
PyQt tools code
usage mode:
    in class
'''

from PyQt5.QtWidgets import QDesktopWidget


def center(self):
    '''
    set the qt windows center
    usage mode:
        call in the init function

    :param self:
    :return:
    '''

    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())


from PyQt5.QtWidgets import QMessageBox


def closeEvent(self, QCloseEvent):
    '''
    add close event
    usage mode:
        add code into class, not call in a function

    :param self:
    :param QCloseEvent:
    :return:
    '''

    reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No)

    if reply == QMessageBox.Yes:
        QCloseEvent.accept()
    else:
        QCloseEvent.ignore()


from PyQt5.QtGui import QPainter


def paintEvent(self, QPaintEvent):
    '''
    add paint event
    usage mode:
        add paint code into class, don't need call in init

    :param self:
    :param QPaintEvent:
    :return:
    '''
    qp = QPainter()
    qp.begin(self)
    # use paint function replace pass
    # add paint code
    pass
    qp.end()