#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Ceausi -> RuleBoxWidget

Author: Remi GASCOU
Last edited: October 2018
"""


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib.ui.widgets.RuleCellNeighborsWidget import *

class RuleBoxWidget(QWidget):
    """docstring for RuleBoxWidget."""
    def __init__(self, ruleName, gridin, gridout, parent=None):
        super(RuleBoxWidget, self).__init__()
        self.parent     = parent
        self.ruleName   = ruleName
        self.gridin     = gridin
        self.gridout    = gridout
        self._initUI()
        self.show()

    def _initUI(self):
        self.layout = QGridLayout()
        self.labelRuleName = QLabel(self.ruleName, self)
        self.layout.addWidget(self.labelRuleName, 0, 0)
        self.cellNeighborsIn = RuleCellNeighborsWidget(self.gridin, self)
        self.layout.addWidget(self.cellNeighborsIn, 0, 1)
        self.cellNeighborsOut = RuleCellNeighborsWidget(self.gridout, self)
        self.layout.addWidget(self.cellNeighborsOut, 0, 2)
        self.setLayout(self.layout)
        self._loadStyleSheet()

    def _loadStyleSheet(self, path="lib/ui/widgets/styles/RuleBoxWidget.css"):
        f = open(path,'r')
        stylesheet = "".join(f.readlines())
        f.close()
        self.setStyleSheet(stylesheet)
