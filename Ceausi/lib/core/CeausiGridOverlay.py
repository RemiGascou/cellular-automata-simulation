#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimlator -> CeausiGridOverlay

Author: Remi GASCOU
Last edited: November 2018
"""

import json
from numpy import array, zeros
from random import choice

class CeausiGridOverlay(object):
    def __init__(self, settings, parent=None):
        super(CeausiGridOverlay, self).__init__()
        self.settings   = settings
        self.grid       = []
        self.cleargrid()

    def regen(self):
        self.grid       = self._generateRandomgrid()

    def cleargrid(self):
        self.grid.clear()
        for _ in range(self.settings.get_gridwidth()):
            self.grid.append([self.settings.get_valueCellOff() for k in range(self.settings.get_gridheight())])

    # *----------------------------- Utils ------------------------------------*

    def drawSquare(self, nodeA, nodeB, value, drawplain=False):
        self.cleargrid()
        if nodeA != nodeB and nodeA[0] != -1 and nodeA[1] != -1 and nodeB[0] != -1 and nodeB[1] != -1:
            print(nodeA[0]-nodeB[0], nodeA[1]-nodeB[1])

            if nodeA[0]-nodeB[0] > 0: nodeA[0], nodeB[0] = nodeB[0], nodeA[0]
            if nodeA[1]-nodeB[1] > 0: nodeA[1], nodeB[1] = nodeB[1], nodeA[1]

            if drawplain == False:
                diffx, diffy = abs(nodeA[0]-nodeB[0]), abs(nodeA[1]-nodeB[1])
                if nodeA[0] != nodeB[0] and nodeA[1] == nodeB[1]:
                    for xk in range(diffx+1):
                        self.grid[nodeA[0] + xk][nodeA[1]] = value
                        self.grid[nodeB[0] + xk][nodeB[1]] = value
                elif nodeA[0] == nodeB[0] and nodeA[1] != nodeB[1]:
                    for yk in range(diffy+1):
                        self.grid[nodeA[0]][nodeA[1] + yk] = value
                        self.grid[nodeB[0]][nodeB[1] + yk] = value
                else :
                    for xk in range(diffx+1):
                        self.grid[nodeA[0] + xk][nodeA[1]] = value
                        self.grid[nodeB[0] - xk][nodeB[1]] = value
                    for yk in range(diffy+1):
                        self.grid[nodeA[0]][nodeA[1] + yk] = value
                        self.grid[nodeB[0]][nodeB[1] - yk] = value
            elif drawplain == True:
                diffx, diffy = abs(nodeA[0]-nodeB[0]), abs(nodeA[1]-nodeB[1])
                if nodeA[0] != nodeB[0] and nodeA[1] == nodeB[1]:
                    for xk in range(diffx+1):
                        self.grid[nodeA[0] + xk][nodeA[1]] = value
                        self.grid[nodeB[0] + xk][nodeB[1]] = value
                elif nodeA[0] == nodeB[0] and nodeA[1] != nodeB[1]:
                    for yk in range(diffy+1):
                        self.grid[nodeA[0]][nodeA[1] + yk] = value
                        self.grid[nodeB[0]][nodeB[1] + yk] = value
                else :
                    for yk in range(diffy+1):
                        for xk in range(diffx+1):
                            self.grid[nodeA[0] + xk][nodeA[1] + yk] = value
                            self.grid[nodeB[0] - xk][nodeB[1] - yk] = value

    # *----------------------------GET--SET------------------------------------*

    def get_grid (self):
        return self.grid

    def set_grid (self, grid):
        self.grid = grid

    def get_settings (self):
        return self.settings

    def set_settings (self, settings):
        self.settings = settings
