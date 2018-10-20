#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimulatorApp -> RulesWindow

Author: Remi GASCOU
Last edited: October 2018
"""

import sys
from lib.core import CellularAutomataSimulatorAppInfos
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class RulesWindow(QWidget):
    def __init__(self, parent=None):
        print("[LOG] Parent of RulesWindow", parent)
        super(RulesWindow, self).__init__()
        self.title = 'RulesWindow'
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
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('lib/meta/ico.png'))
        self.label = QLabel("<b>" + CellularAutomataSimulatorAppInfos.get_name() + " - " + CellularAutomataSimulatorAppInfos.get_versiontag() + " </b><br><br>" + CellularAutomataSimulatorAppInfos.get_credits(), self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 300, 100)
        self.setFixedSize(self.size())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RulesWindow()
    sys.exit(app.exec_())
