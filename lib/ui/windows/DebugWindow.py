#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimulatorApp -> DebugWindow

Author: Remi GASCOU
Last edited: October 2018
"""

import sys
from lib.core import CellularAutomataSimulatorAppInfos
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DebugWindow(QWidget):
    def __init__(self, parent=None):
        print("[LOG] Parent of DebugWindow", parent)
        super(DebugWindow, self).__init__()
        self.title = "DebugWindow"
        self._initUI()
        self.show()

    def _initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('lib/meta/ico.png'))
        self.layout = QFormLayout()
        self.pushbutton_addtab = QPushButton("Add Tab")
        self.pushbutton_addtab.clicked.connect(self.none)
        self.layout.addRow("Add Tab", self.pushbutton_addtab)
        self.pushbutton_deltab = QPushButton("Del Tab")
        self.pushbutton_deltab.clicked.connect(self.none)
        self.layout.addRow("Del Tab", self.pushbutton_deltab)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 300, 100)

    @pyqtSlot()
    def none(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DebugWindow()
    sys.exit(app.exec_())
