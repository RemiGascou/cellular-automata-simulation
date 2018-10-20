# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib.core.CeausiGrid import *

class CeausiCanvas(QWidget):
    def __init__(self, cellsize=20, gridx=10, gridy=10, parent=None):
        super(CeausiCanvas, self).__init__()
        self.cellsize   = cellsize
        self.colorLine  = [175,175,175]
        self.colorOn    = [100,100,255]
        self.colorOff   = [255,255,255]
        self.valueOn      = 0
        self.valueOff     = 1
        self.ceausi_grid  = CeausiGrid()
        self.ceausi_grid.gridheight = gridx
        self.ceausi_grid.gridwidth  = gridy
        self.ceausi_grid.cleargrid()

        self.__oldmouseMovePos_x = -1
        self.__oldmouseMovePos_y = -1
        self.__begSquare         = [-1,-1]
        self.__endSquare         = [-1,-1]
        self._drawMode           = 1

    def regen(self):
        self.ceausi_grid.regen()
        self.update()

    def cleargrid(self):
        self.ceausi_grid.cleargrid()
        self.update()

    def _updateUI(self):
        self.update()

    def updateGrid(self):
        if len(self.ceausi_grid.grid) != 0:
            self.ceausi_grid.updateGrid()
            self.update()

    def paintEvent(self, e):
        if len(self.ceausi_grid.grid) != 0:
            qp = QPainter(self)
            qp.setPen(QColor(self.colorLine[0], self.colorLine[1], self.colorLine[2]))
            for xk in range(len(self.ceausi_grid.grid)):
                for yk in range(len(self.ceausi_grid.grid[0])):
                    if self.ceausi_grid.grid[xk][yk] == self.valueOn:
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
                    self.ceausi_grid.grid[self.__begSquare[0] + xk][self.__begSquare[1]] = 1 ^ self.ceausi_grid.grid[self.__begSquare[0] + xk][self.__begSquare[1]]
                    self.ceausi_grid.grid[self.__endSquare[0] + xk][self.__endSquare[1]] = 1 ^ self.ceausi_grid.grid[self.__endSquare[0] + xk][self.__endSquare[1]]
            elif self.__begSquare[0] == self.__endSquare[0] and self.__begSquare[1] != self.__endSquare[1]:
                print('Tracé y')
                for yk in range(diffy):
                    self.ceausi_grid.grid[self.__begSquare[0]][self.__begSquare[1] + yk] = 1 ^ self.ceausi_grid.grid[self.__begSquare[0]][self.__begSquare[1] + yk]
                    self.ceausi_grid.grid[self.__endSquare[0]][self.__endSquare[1] + yk] = 1 ^ self.ceausi_grid.grid[self.__endSquare[0]][self.__endSquare[1] + yk]
            else :
                print('Tracé xy')
                for xk in range(diffx):
                    self.ceausi_grid.grid[self.__begSquare[0] + xk][self.__begSquare[1]] = 1 ^ self.ceausi_grid.grid[self.__begSquare[0] + xk][self.__begSquare[1]]
                    self.ceausi_grid.grid[self.__endSquare[0] + xk][self.__endSquare[1]] = 1 ^ self.ceausi_grid.grid[self.__endSquare[0] + xk][self.__endSquare[1]]
                for yk in range(diffy):
                    self.ceausi_grid.grid[self.__begSquare[0]][self.__begSquare[1] + yk] = 1 ^ self.ceausi_grid.grid[self.__begSquare[0]][self.__begSquare[1] + yk]
                    self.ceausi_grid.grid[self.__endSquare[0]][self.__endSquare[1] + yk] = 1 ^ self.ceausi_grid.grid[self.__endSquare[0]][self.__endSquare[1] + yk]
            self.update()

    def mousePressEvent(self, event):
        #print('mousePressEvent at :', max(min(event.x()//self.cellsize, self.ceausi_grid.gridheight-1), 0), max(min(event.y()//self.cellsize, self.ceausi_grid.gridwidth-1), 0))
        if event.buttons() == Qt.RightButton:
            self.__begSquare = [max(min(event.x()//self.cellsize, self.ceausi_grid.gridheight-1), 0), max(min(event.y()//self.cellsize, self.ceausi_grid.gridwidth-1), 0)]
        elif event.buttons() == Qt.LeftButton:
            self.__oldmouseMovePos_x = max(min(event.x()//self.cellsize, self.ceausi_grid.gridheight-1), 0)
            self.__oldmouseMovePos_y = max(min(event.y()//self.cellsize, self.ceausi_grid.gridwidth-1), 0)
            self.ceausi_grid.grid[max(min(event.x()//self.cellsize, self.ceausi_grid.gridheight-1), 0)][max(min(event.y()//self.cellsize, self.ceausi_grid.gridwidth-1), 0)] = 1 ^ self.ceausi_grid.grid[max(min(event.x()//self.cellsize, self.ceausi_grid.gridheight-1), 0)][max(min(event.y()//self.cellsize, self.ceausi_grid.gridwidth-1), 0)]
            self.update()

    def mouseReleaseEvent(self, event):
        #print('mouseReleaseEvent')
        #if event.buttons() == Qt.RightButton:
        self.__endSquare = [max(min(event.x()//self.cellsize, self.ceausi_grid.gridheight-1), 0), max(min(event.y()//self.cellsize, self.ceausi_grid.gridwidth-1), 0)]
        #print('Drawing Square between', self.__begSquare, self.__endSquare)
        #self.__drawSquare()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.__oldmouseMovePos_x != max(min(event.x()//self.cellsize, self.ceausi_grid.gridheight-1), 0) or self.__oldmouseMovePos_y != max(min(event.y()//self.cellsize, self.ceausi_grid.gridwidth-1), 0) :
                self.ceausi_grid.grid[max(min(event.x()//self.cellsize, self.ceausi_grid.gridheight-1), 0)][max(min(event.y()//self.cellsize, self.ceausi_grid.gridwidth-1), 0)] = 1 ^ self.ceausi_grid.grid[max(min(event.x()//self.cellsize, self.ceausi_grid.gridheight-1), 0)][max(min(event.y()//self.cellsize, self.ceausi_grid.gridwidth-1), 0)]
                self.update()
            self.__oldmouseMovePos_x = max(min(event.x()//self.cellsize, self.ceausi_grid.gridheight-1), 0)
            self.__oldmouseMovePos_y = max(min(event.y()//self.cellsize, self.ceausi_grid.gridwidth-1), 0)


    # *------------------------openFileNameDialog------------------------------*

    def openGridFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open Grid File", "","Ceausi Grid Files (*.casgrid)", options=options)
        if fileName:
            self.ceausi_grid.loadGridFromFile(fileName)

    def saveGridFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Grid","","Ceausi Grid Files (*.casgrid)", options=options)
        if fileName:
            self.ceausi_grid.saveGridToFile(fileName)



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
        return self.ceausi_grid.grid

    def set_grid (self, grid):
        self.ceausi_grid.grid = grid

    def get_gridheight (self):
        return self.ceausi_grid.gridheight

    def set_gridheight (self, gridheight):
        self.ceausi_grid.gridheight = max(0,gridheight)

    def get_gridwidth (self):
        return self.ceausi_grid.gridwidth

    def set_gridwidth (self, gridwidth):
        self.ceausi_grid.gridwidth = max(0,gridwidth)

    def get_cellsize (self):
        return self.cellsize

    def set_cellsize (self, cellsize):
        self.cellsize = max(0,cellsize)
