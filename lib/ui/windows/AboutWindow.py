#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyChat -> AboutWindow

Author: Remi GASCOU
Last edited: July 2018
"""

import sys
from lib.core import PyChatInfos
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class AboutWindow(QWidget):
    def __init__(self, parent=None):
        print("[LOG] Parent of AboutWindow", parent)
        super(AboutWindow, self).__init__()
        self.title = 'AboutWindow'
        self.left   = 0
        self.top    = 0
        self.width  = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)  #Kill application on close
        self.setGeometry(self.left, self.top, self.width, self.height)
        self._initUI()
        self.show()

    def _initUI(self):
        self.label = QLabel("<b>" + PyChatInfos.get_name() + " " + PyChatInfos.get_version() + " </b><br><br>" + PyChatInfos.get_credits(), self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('About')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AboutWindow()
    sys.exit(app.exec_())
