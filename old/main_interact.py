# -*- coding: utf-8 -*-

import os, sys
from numpy import array, zeros
from random import choice

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ConwayCanvas(QWidget):
    def __init__(self, cellsize=20, gridx=10, gridy=10, parent=None):
        super(ConwayCanvas, self).__init__()
        self.gridheight = gridx
        self.gridwidth  = gridy
        self.cellsize   = cellsize
        self.colorLine  = [175,175,175]
        self.colorOn    = [100,100,255]
        self.colorOff   = [255,255,255]

        self.valueOn    = 0
        self.valueOff   = 1
        self.grid           = self._generateRandomgrid()
        self.old_grid       = [[self.valueOff]*self.gridwidth]*self.gridheight
        self.old_old_grid   = [[self.valueOff]*self.gridwidth]*self.gridheight

    def regen(self):
        self.grid           = self._generateRandomgrid()
        self.old_grid       = [[self.valueOff]*self.gridwidth]*self.gridheight
        self.old_old_grid   = [[self.valueOff]*self.gridwidth]*self.gridheight
        self.update()

    def cleargrid(self):
        self.grid           = [[self.valueOff]*self.gridwidth]*self.gridheight
        self.old_grid       = [[self.valueOff]*self.gridwidth]*self.gridheight
        self.old_old_grid   = [[self.valueOff]*self.gridwidth]*self.gridheight
        self.applyRules()
        self.update()

    def updateGridEvent(self):
        if len(self.grid) != 0:
            self.old_old_grid = self.old_grid.copy()
            self.old_grid = self.grid.copy()
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

    def mousePressEvent(self, event):
        self.grid[event.x()//self.cellsize][event.y()//self.cellsize] = 1 ^ self.grid[event.x()//self.cellsize][event.y()//self.cellsize]
        self.update()


    def _getNeighbours(self, x, y):
        """
            Function that, for a given self.grid and a given cell, identified with its coordinates x and y, return the coordinates and values of its neighbours
            Parameters :
                - self.grid : a n x m array with the values of each cell, dead or alive
                - x : the coordinate of the cell on the x-axis
                - y : the coordinate of the cell on the y-axis
            Return :
                - neighbours : a dictionnary containing the coordinates and the values of the neighbours of the cell
            Note : to access to the value of a given cell neighbour, use 'neighbours[x][y]', considering that 'neighbours' is returned by the function and 'x' and 'y' are the coordinates of the cell of which we want to have access
        """
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
        """
            Function that, for a given self.grid and a given cell, identified with its coordinates x and y, return the number of cells in its neighbourhood that are on and the number that are off
            Parameters :
                - self.grid : a n x m array with the values of each cell, dead or alive
                - x : the coordinate of the cell on the x-axis
                - y : the coordinate of the cell on the y-axis
                - self.valueOn : the value that code the fact that a cell is on
                - self.valueOff : the value that code the fact that a cell is off
            Return :
                - numberOn, numberOff : the number of cells that are on and off in the neighbourhood
        """
        numberOn, numberOff = 0, 0
        neighbours = self._getNeighbours(x, y)
        for key in neighbours.keys(): # we go through all the keys in the dict, so all the coordinates of the neighbours
            if(neighbours[key] == self.valueOn):
                numberOn += 1
            elif(neighbours[key] == self.valueOff):
                numberOff += 1
        return numberOn, numberOff

    def applyRules(self):
        """
            Function that, for a given grid, apply the rules of the game (see below for the detail)
            Parameters :
                - self.grid : a n x m array with the values of each cell, dead or alive
                - self.valueOn : the value that code the fact that a cell is on
                - self.valueOff : the value that code the fact that a cell is off
            Return :
                - nextgrid : the self.grid updated with the rules of the game (see below for the detail)
            Note : the rules are the following
                1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
                2. Any live cell with two or three live neighbours lives on to the next generation.
                3. Any live cell with more than three live neighbours dies, as if by overpopulation.
                4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
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
        """
            Function that generate randomly a self.grid
            Parameters :
                - xSize : the size of the self.grid on the x-axis
                - ySize : the size of the self.grid on the x-axis
                - self.valueOn : the value that code the fact that a cell is on
                - self.valueOff : the value that code the fact that a cell is off
            Return :
                - self.grid : the self.grid generated randomly
        """
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


class ConwaysApp(QMainWindow):
    """docstring for ConwaysApp."""
    def __init__(self, gridx=10, gridy=10, parent=None):
        super(ConwaysApp, self).__init__()
        self.title  = "Conway's Game of Life"
        self.gridx  = gridx
        self.gridy  = gridy
        self.cellsize = 25
        self.left   = 10
        self.top    = 10
        self.width  = self.gridx*self.cellsize
        self.height = self.gridy*self.cellsize
        self._initUI()
        self.timer_period = 125
        self.timer_state  = False
        self.timer  = QTimer()
        self.timer.timeout.connect(self.conway_grid.updateGridEvent)

    def _initUI(self):
        self.setWindowTitle(self.title + " - [PAUSED]")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.size())
        self.setAttribute(Qt.WA_DeleteOnClose)
        #Trick to center window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        #EndTrick
        self.conway_grid = ConwayCanvas(self.cellsize, self.gridx, self.gridy)
        self.setCentralWidget(self.conway_grid)
        self.show()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            if self.timer_state == True :
                self.timer_state = False
                self.timer.stop()
                self.setWindowTitle(self.title +" - [PAUSED]")
            else :
                self.timer_state = True
                self.timer.start(self.timer_period)
                self.setWindowTitle(self.title)
        elif event.key() == Qt.Key_R:
            self.conway_grid.regen()
        elif event.key() == Qt.Key_C:
            self.conway_grid.cleargrid()

if __name__ == """__main__""":
    app = QApplication(sys.argv)
    ex = ConwaysApp(38,20) #76,40
    sys.exit(app.exec_())

# Key_C to clear grid
# Key_Space to toggle running
# Key_R to regen grid
