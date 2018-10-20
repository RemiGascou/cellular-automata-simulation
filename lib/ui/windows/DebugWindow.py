#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyChat -> DebugWindow

Author: Remi GASCOU
Last edited: July 2018
"""

import sys
from lib.core import PyChatInfos
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DebugWindow(QWidget):
    def __init__(self, parent=None):
        print("[LOG] Parent of DebugWindow", parent)
        super(DebugWindow, self).__init__()
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('About')
        self._initUI()
        self.show()

    def _initUI(self):
        self.layout = QFormLayout()
        self.pushbutton_addtab = QPushButton("Add Tab")
        self.pushbutton_addtab.clicked.connect(self.none)
        self.layout.addRow("Add Tab", self.pushbutton_addtab)
        self.pushbutton_deltab = QPushButton("Del Tab")
        self.pushbutton_deltab.clicked.connect(self.none)
        self.layout.addRow("Del Tab", self.pushbutton_deltab)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('Connect')

    @pyqtSlot()
    def none(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DebugWindow()
    sys.exit(app.exec_())
