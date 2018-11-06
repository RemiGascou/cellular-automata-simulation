#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimulatorApp -> RuleCellNeighborsWidget

Author: Remi GASCOU
Last edited: October 2018
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class RuleCellNeighborsWidget(QWidget):
    """docstring for RuleCellNeighborsWidget."""
    def __init__(self, grid, parent=None):
        super(RuleCellNeighborsWidget, self).__init__()
        self.parent     = parent
        if len(grid) == 3:
            if len(grid[0]) == 3:
                self.grid = grid
            else:
                self.grid = [[0,0,0], [0,0,0], [0,0,0]]
        else :
            self.grid = [[0,0,0], [0,0,0], [0,0,0]]

        self.cellsize     = 20
        self.colorLine    = [175,175,175]
        self.colorOn      = [100,100,255]
        self.colorOff     = [255,255,255]
        self.colorBlocked = [175,175,175]
        self.valueOn      = 1
        self.valueOff     = 0
        #self.show()

    def paintEvent(self, e):
        qp = QPainter(self)
        qp.setPen(QColor(self.colorLine[0], self.colorLine[1], self.colorLine[2]))
        for xk in range(len(self.grid)):
            for yk in range(len(self.grid[0])):
                if self.grid[xk][yk] == self.valueOn:
                    qp.setBrush(QColor(self.colorOn[0], self.colorOn[1], self.colorOn[2]))
                else :
                    qp.setBrush(QColor(self.colorOff[0], self.colorOff[1], self.colorOff[2]))
                #if xk == 1 and yk == 1:
                #    qp.setBrush(QColor(self.colorBlocked[0], self.colorBlocked[1], self.colorBlocked[2]))
                qp.drawRect(self.cellsize*xk, self.cellsize*yk, self.cellsize, self.cellsize)
