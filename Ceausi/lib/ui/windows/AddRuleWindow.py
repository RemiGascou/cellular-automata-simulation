#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimulatorApp -> AddRuleWindow

Author: Remi GASCOU
Last edited: October 2018
"""

import sys
from lib.core import CellularAutomataSimulatorAppInfos
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class AddRuleWindow(QWidget):
    def __init__(self, parent=None):
        #print("[LOG] Parent of AddRuleWindow", parent)
        super(AddRuleWindow, self).__init__()
        self.title = 'AddRuleWindow'
        self.left   = 0
        self.top    = 0
        self.width  = 460
        self.height = 500
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
        self.setGeometry(300, 300, self.width, self.height)
        self.setFixedSize(self.size())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddRuleWindow()
    sys.exit(app.exec_())
