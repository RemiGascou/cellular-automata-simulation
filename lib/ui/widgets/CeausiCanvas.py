# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from numpy import array, zeros
from random import choice

from lib.core.CeausiGrid import *

class CeausiCanvas(QWidget):
    def __init__(self, cellsize=20, gridx=10, gridy=10, parent=None):
        super(CeausiCanvas, self).__init__()
        self.gridheight = gridx
        self.gridwidth  = gridy
        self.cellsize   = cellsize
        self.colorLine  = [175,175,175]
        self.colorOn    = [100,100,255]
        self.colorOff   = [255,255,255]

        self.valueOn    = 0
        self.valueOff   = 1
        self.grid       = []
        self.cleargrid()

        self.__oldmouseMovePos_x = -1
        self.__oldmouseMovePos_y = -1
        self.__begSquare         = [-1,-1]
        self.__endSquare         = [-1,-1]
        self._drawMode           = 1

    def regen(self):
        self.grid           = self._generateRandomgrid()
        self.update()

    def cleargrid(self):
        self.grid           = [[self.valueOff]*self.gridwidth]*self.gridheight
        self.applyRules()
        self.update()

    def _updateUI(self):
        self.update()

    def updateGridEvent(self):
        if len(self.grid) != 0:
            self.applyRules()
            self.update()

    def paintEvent(self, e):
        if len(self.grid) != 0:
            qp = QPainter(self)
            qp.setPen(QColor(self.colorLine[0], self.colorLine[1], self.colorLine[2]))
            for xk in range(len(self.grid)):
                for yk in range(len(self.grid[0])):
                    if self.grid[xk][yk] == self.valueOn:
                        qp.setBrush(QColor(self.colorOn[0], self.colorOn[1], self.colorOn[2]))
                    else :
                        qp.setBrush(QColor(self.colorOff[0], self.colorOff[1], self.colorOff[2]))
                    qp.drawRect(self.cellsize*xk, self.cellsize*yk, self.cellsize*(xk+1), self.cellsize*(yk+1))

    def __drawSquare(self): #Problem
        if self.__begSquare != self.__endSquare and self.__begSquare[0] != -1 and self.__begSquare[1] != -1 and self.__endSquare[0] != -1 and self.__endSquare[1] != -1:
            diffx, diffy = abs(self.__begSquare[0]-self.__endSquare[0]), abs(self.__begSquare[1]-self.__endSquare[1])
            if self.__begSquare[0] != self.__endSquare[0] and self.__begSquare[1] == self.__endSquare[1]:
                print('Tracé x')
                for xk in range(diffx):
                    self.grid[self.__begSquare[0] + xk][self.__begSquare[1]] = 1 ^ self.grid[self.__begSquare[0] + xk][self.__begSquare[1]]
                    self.grid[self.__endSquare[0] + xk][self.__endSquare[1]] = 1 ^ self.grid[self.__endSquare[0] + xk][self.__endSquare[1]]
            elif self.__begSquare[0] == self.__endSquare[0] and self.__begSquare[1] != self.__endSquare[1]:
                print('Tracé y')
                for yk in range(diffy):
                    self.grid[self.__begSquare[0]][self.__begSquare[1] + yk] = 1 ^ self.grid[self.__begSquare[0]][self.__begSquare[1] + yk]
                    self.grid[self.__endSquare[0]][self.__endSquare[1] + yk] = 1 ^ self.grid[self.__endSquare[0]][self.__endSquare[1] + yk]
            else :
                print('Tracé xy')
                for xk in range(diffx):
                    self.grid[self.__begSquare[0] + xk][self.__begSquare[1]] = 1 ^ self.grid[self.__begSquare[0] + xk][self.__begSquare[1]]
                    self.grid[self.__endSquare[0] + xk][self.__endSquare[1]] = 1 ^ self.grid[self.__endSquare[0] + xk][self.__endSquare[1]]
                for yk in range(diffy):
                    self.grid[self.__begSquare[0]][self.__begSquare[1] + yk] = 1 ^ self.grid[self.__begSquare[0]][self.__begSquare[1] + yk]
                    self.grid[self.__endSquare[0]][self.__endSquare[1] + yk] = 1 ^ self.grid[self.__endSquare[0]][self.__endSquare[1] + yk]
            self.update()

    def mousePressEvent(self, event):
        #print('mousePressEvent')
        if event.buttons() == Qt.RightButton:
            self.__begSquare = [max(min(event.x()//self.cellsize, self.gridheight-1), 0), max(min(event.y()//self.cellsize, self.gridwidth-1), 0)]
        elif event.buttons() == Qt.LeftButton:
            self.__oldmouseMovePos_x = max(min(event.x()//self.cellsize, self.gridheight-1), 0)
            self.__oldmouseMovePos_y = max(min(event.y()//self.cellsize, self.gridwidth-1), 0)
            self.grid[max(min(event.x()//self.cellsize, self.gridheight-1), 0)][max(min(event.y()//self.cellsize, self.gridwidth-1), 0)] = 1 ^ self.grid[max(min(event.x()//self.cellsize, self.gridheight-1), 0)][max(min(event.y()//self.cellsize, self.gridwidth-1), 0)]
            self.update()

    def mouseReleaseEvent(self, event):
        #print('mouseReleaseEvent')
        #if event.buttons() == Qt.RightButton:
        self.__endSquare = [max(min(event.x()//self.cellsize, self.gridheight-1), 0), max(min(event.y()//self.cellsize, self.gridwidth-1), 0)]
        #print('Drawing Square between', self.__begSquare, self.__endSquare)
        #self.__drawSquare()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.__oldmouseMovePos_x != max(min(event.x()//self.cellsize, self.gridheight-1), 0) or self.__oldmouseMovePos_y != max(min(event.y()//self.cellsize, self.gridwidth-1), 0) :
                self.grid[max(min(event.x()//self.cellsize, self.gridheight-1), 0)][max(min(event.y()//self.cellsize, self.gridwidth-1), 0)] = 1 ^ self.grid[max(min(event.x()//self.cellsize, self.gridheight-1), 0)][max(min(event.y()//self.cellsize, self.gridwidth-1), 0)]
                self.update()
            self.__oldmouseMovePos_x = max(min(event.x()//self.cellsize, self.gridheight-1), 0)
            self.__oldmouseMovePos_y = max(min(event.y()//self.cellsize, self.gridwidth-1), 0)


    def _getNeighbours(self, x, y):
        neighbours = {}
        if (x == 0):
            if (y == 0): # Upper left corner
                neighbours = {(x,y+1):self.grid[x][y+1],(x+1,y):self.grid[x+1][y],(x+1,y+1):self.grid[x+1][y+1]}
            elif (y == len(self.grid[0])-1): # Upper right corner
                neighbours = {(x,y-1):self.grid[x][y-1],(x+1,y):self.grid[x+1][y],(x+1,y-1):self.grid[x+1][y-1]}
            else: # Upper border
                neighbours = {(x,y-1):self.grid[x][y-1],(x,y+1):self.grid[x][y+1],(x+1,y-1):self.grid[x+1][y-1],(x+1,y):self.grid[x+1][y],(x+1,y+1):self.grid[x+1][y-1]}
        elif (x == len(self.grid)-1):
            if (y == 0): # Left down corner
                neighbours = {(x-1,y):self.grid[x-1][y],(x,y+1):self.grid[x][y+1],(x-1,y+1):self.grid[x-1][y+1]}
            elif (y == len(self.grid[0])-1): # Right down corner
                neighbours = {(x,y-1):self.grid[x][y-1],(x-1,y):self.grid[x-1][y],(x-1,y-1):self.grid[x-1][y-1]}
            else: # Down border
                neighbours = {(x,y+1):self.grid[x][y+1],(x,y-1):self.grid[x][y-1],(x-1,y-1):self.grid[x-1][y-1],(x-1,y):self.grid[x-1][y],(x-1,y+1):self.grid[x-1][y+1]}
        else:
            if(y == 0): # Left border
                neighbours = {(x-1,y):self.grid[x-1][y],(x+1,y):self.grid[x+1][y],(x-1,y+1):self.grid[x-1][y+1],(x,y+1):self.grid[x][y+1],(x+1,y+1):self.grid[x+1][y+1]}
            elif(y == len(self.grid[0])-1): # Right border
                neighbours = {(x-1,y):self.grid[x-1][y],(x+1,y):self.grid[x+1][y],(x-1,y-1):self.grid[x-1][y-1],(x,y-1):self.grid[x][y-1],(x+1,y-1):self.grid[x+1][y-1]}
            else: # Middle
                neighbours = {(x-1,y-1):self.grid[x-1][y-1],(x-1,y):self.grid[x-1][y],(x-1,y+1):self.grid[x-1][y+1],(x,y-1):self.grid[x][y-1],(x,y+1):self.grid[x][y+1],(x+1,y-1):self.grid[x+1][y-1],(x+1,y):self.grid[x+1][y],(x+1,y+1):self.grid[x+1][y+1]}
        neighbours.update({(x,y):2}) # Add the value of the cell for which we look the neighbours, make sure not to use the value 2 for either self.valueOn and self.valueOff as it's used here
        return neighbours

    def _countNeighbours(self, x, y):
        numberOn, numberOff = 0, 0
        neighbours = self._getNeighbours(x, y)
        for key in neighbours.keys(): # we go through all the keys in the dict, so all the coordinates of the neighbours
            if(neighbours[key] == self.valueOn):
                numberOn += 1
            elif(neighbours[key] == self.valueOff):
                numberOff += 1
        return numberOn, numberOff

    def applyRules(self):
        nextgrid = [[self.valueOff for y in range(len(self.grid[0]))] for x in range(len(self.grid))]
        for x in range(len(self.grid)): # we go through all the point on the x-axis
            for y in range(len(self.grid[0])): # we go through all the point on the y-axis
                numberOn, numberOff = self._countNeighbours(x, y)
                if(self.grid[x][y] == self.valueOn): # For the rules 1, 2 and 3
                    if(numberOn < 2): # For the rule 1
                        nextgrid[x][y] = self.valueOff
                    elif(numberOn == 2 or numberOn == 3): # For the rule 2
                        nextgrid[x][y] = self.valueOn
                    elif(numberOn > 3): # For the rule 3
                        nextgrid[x][y] = self.valueOff
                elif(self.grid[x][y] == self.valueOff and numberOn == 3): # For the rule 4
                    nextgrid[x][y] = self.valueOn
        self.grid = nextgrid

    def _generateRandomgrid(self):
        self.grid = zeros((self.gridheight, self.gridwidth), dtype=int)
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                self.grid[x][y] = choice([self.valueOn, self.valueOff]) # for each cell, we choose randomly a value between self.valueOn and self.valueOff
        return self.grid


    # *----------------------------GET--SET------------------------------------*
    def get_valueOn (self):
        return self.valueOn

    def set_valueOn (self, valueOn):
        self.valueOn = valueOn

    def get_valueOff (self):
        return self.valueOff

    def set_valueOff (self, valueOff):
        self.valueOff = valueOff

    def get_colorOn (self):
        return self.colorOn

    def set_colorOn (self, colorOn):
        self.colorOn = colorOn

    def get_colorOff (self):
        return self.colorOff

    def set_colorOff (self, colorOff):
        self.colorOff = colorOff

    def get_grid (self):
        return self.grid

    def set_grid (self, grid):
        self.grid = grid

    def get_gridheight (self):
        return self.gridheight

    def set_gridheight (self, gridheight):
        self.gridheight = max(0,gridheight)

    def get_gridwidth (self):
        return self.gridwidth

    def set_gridwidth (self, gridwidth):
        self.gridwidth = max(0,gridwidth)

    def get_cellsize (self):
        return self.cellsize

    def set_cellsize (self, cellsize):
        self.cellsize = max(0,cellsize)
