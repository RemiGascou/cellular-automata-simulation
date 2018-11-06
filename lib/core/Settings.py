#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimlator -> Settings

Author: Remi GASCOU
Last edited: November 2018
"""

from PyQt5.QtGui import QColor

class Settings(object):
    """docstring for Settings."""
    def __init__(self):
        super(Settings, self).__init__()
        self.timer_period       = 125     #ms
        self.cellsize           = 12      #px
        self.drawmode           = 0
        self.valueCellOn        = 1
        self.valueCellOff       = 0
        self.gridheight         = 0
        self.gridwidth          = 0
        #Colors
        self.colorGridLine      = [175,175,175]
        self.colorCellOn        = [255,255,255]
        self.colorCellOff       = [0,0,0]
        self.colorCellOverlay   = [255,100,100]

# *----------------------------------Get Set------------------------[Values]-- *

    def get_valueCellOn (self):
        return self.valueCellOn

    def set_valueCellOn (self, valueCellOn):
        self.valueCellOn = valueCellOn

    def get_valueCellOff (self):
        return self.valueCellOff

    def set_valueCellOff (self, valueCellOff):
        self.valueCellOff = valueCellOff

    def get_cellsize (self):
        return self.cellsize

    def set_cellsize (self, cellsize):
        self.cellsize = cellsize

    def get_timerperiod (self):
        return self.timer_period

    def set_timerperiod (self, timer_period):
        self.timer_period = timer_period

    def get_gridheight (self):
        return self.gridheight

    def set_gridheight (self, gridheight):
        self.gridheight = gridheight

    def get_gridwidth (self):
        return self.gridwidth

    def set_gridwidth (self, gridwidth):
        self.gridwidth = gridwidth



    def get_drawmode (self):
        return self.drawmode

    def set_drawmode (self, drawmode):
        self.drawmode = drawmode


# *----------------------------------Get Set------------------------[Colors]-- *

    def get_QColorGridLine (self):
        return QColor(self.colorGridLine[0], self.colorGridLine[1], self.colorGridLine[2])

    def get_colorGridLine (self):
        return self.colorGridLine

    def set_colorGridLine (self, r, g, b):
        self.colorGridLine = [max(min(r, 255), 0), max(min(g, 255), 0), max(min(b, 255), 0)]

    def get_QColorCellOn (self):
        return QColor(self.colorCellOn[0], self.colorCellOn[1], self.colorCellOn[2])

    def get_colorCellOn (self):
        return self.colorCellOn

    def set_colorCellOn (self, r, g, b):
        self.colorCellOn = [max(min(r, 255), 0), max(min(g, 255), 0), max(min(b, 255), 0)]

    def get_QColorCellOff (self):
        return QColor(self.colorCellOff[0], self.colorCellOff[1], self.colorCellOff[2])

    def get_colorCellOff (self):
        return self.colorCellOff

    def set_colorCellOff (self, r, g, b):
        self.colorCellOff = [max(min(r, 255), 0), max(min(g, 255), 0), max(min(b, 255), 0)]

    def get_QColorCellOverlay (self):
        return QColor(self.colorCellOverlay[0], self.colorCellOverlay[1], self.colorCellOverlay[2])

    def get_colorCellOverlay (self):
        return self.colorCellOverlay

    def set_colorCellOverlay (self, r, g, b):
        self.colorCellOverlay = [max(min(r, 255), 0), max(min(g, 255), 0), max(min(b, 255), 0)]
