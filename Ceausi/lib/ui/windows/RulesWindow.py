#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimulatorApp -> RulesWindow

Author: Remi GASCOU
Last edited: October 2018
"""

import sys
from lib.core import CellularAutomataSimulatorAppInfos
from lib.ui.widgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class RulesWindow(QWidget):
    def __init__(self, parent=None):
        #print("[LOG] Parent of RulesWindow", parent)
        super(RulesWindow, self).__init__()
        self.title       = 'RulesWindow'
        self.margin_left = 150
        self.margin_top  = 150
        self.width       = 460
        self.height      = 500
        self._initUI()
        self.show()

    def _initUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)  #Kill application on close
        self.setGeometry(self.margin_top, self.margin_left, self.width, self.height)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('lib/meta/ico.png'))
        #
        self.layout = QGridLayout()
        for k in range(10):
            self.obj = RuleBoxWidget("Rule no " + str(k),[[0,0,0], [0,0,0], [0,0,0]], [[0,1,0], [1,0,1], [0,1,0]], self)
            self.layout.addWidget(self.obj, k, 0)
        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RulesWindow()
    sys.exit(app.exec_())
