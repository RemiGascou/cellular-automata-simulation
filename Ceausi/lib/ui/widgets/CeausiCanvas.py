#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimlator -> CeausiCanvas

Author: Remi GASCOU
Last edited: November 2018
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib.core.CeausiGrid import *
from lib.core.CeausiGridOverlay import *
from lib.core.CeausiElement import *

class CeausiCanvas(QWidget):
    def __init__(self, settings, parent=None):
        super(CeausiCanvas, self).__init__()
        self.settings       = settings
        self.ceausi_element = CeausiElement()
        self.ceausi_grid            = CeausiGrid(self.settings)
        self.ceausi_overlay_grid    = CeausiGridOverlay(self.settings)
        self.ceausi_grid.cleargrid()

        self.__mouseMovePos_x    = -1
        self.__mouseMovePos_y    = -1
        self.__oldmouseMovePos_x = -1
        self.__oldmouseMovePos_y = -1
        self.__begSquare         = [-1,-1]
        self.__endSquare         = [-1,-1]
        self.__drawSquareMode    = 0

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
        if self.settings.get_currentmode() == self.settings.get_drawmodeID():
            if len(self.ceausi_grid.grid) != 0:
                qp = QPainter(self)
                qp.setPen(self.settings.get_QColorGridLine())
                for xk in range(len(self.ceausi_grid.grid)):
                    for yk in range(len(self.ceausi_grid.grid[0])):
                        if self.ceausi_grid.grid[xk][yk] == self.settings.get_valueCellOn():
                            qp.setBrush(self.settings.get_QColorCellOn())
                        else :
                            qp.setBrush(self.settings.get_QColorCellOff())
                        qp.drawRect(self.settings.get_cellsize()*xk, self.settings.get_cellsize()*yk, self.settings.get_cellsize(), self.settings.get_cellsize())
        elif self.settings.get_currentmode() == self.settings.get_selectionmodeID():
            print("paintEvent :: selectionmode", len(self.ceausi_overlay_grid.grid))
            qp = QPainter(self)
            if len(self.ceausi_grid.grid) != 0:
                qp.setPen(self.settings.get_QColorGridLine())
                qp.setBrush(self.settings.get_QColorCellOff())
                for xk in range(len(self.ceausi_grid.grid)):
                    for yk in range(len(self.ceausi_grid.grid[0])):
                        if self.ceausi_grid.grid[xk][yk] == self.settings.get_valueCellOff():
                            qp.setBrush(self.settings.get_QColorCellOff())
                            qp.drawRect(self.settings.get_cellsize()*xk, self.settings.get_cellsize()*yk, self.settings.get_cellsize(), self.settings.get_cellsize())
            if len(self.ceausi_overlay_grid.grid) != 0:
                for xk in range(len(self.ceausi_overlay_grid.grid)):
                    for yk in range(len(self.ceausi_overlay_grid.grid[0])):
                        if self.ceausi_overlay_grid.grid[xk][yk] == self.settings.get_valueCellOn():
                            if self.ceausi_grid.grid[xk][yk] == self.settings.get_valueCellOn(): qp.setBrush(self.settings.get_QColorCellOn())
                            else: qp.setBrush(self.settings.get_QColorCellOverlay())
                            qp.drawRect(self.settings.get_cellsize()*xk, self.settings.get_cellsize()*yk, self.settings.get_cellsize(), self.settings.get_cellsize())


    def mousePressEvent(self, event):
        if self.settings.get_currentmode() == self.settings.get_drawmodeID():
            if event.buttons() == Qt.RightButton:
                self.__drawSquareMode = 1
                self.__begSquare = [max(min(event.x()//self.settings.get_cellsize(), self.settings.get_gridwidth()-1), 0), max(min(event.y()//self.settings.get_cellsize(), self.settings.get_gridheight()-1), 0)]
            elif event.buttons() == Qt.LeftButton:
                self.__oldmouseMovePos_x = max(min(event.x()//self.settings.get_cellsize(), self.settings.get_gridwidth()-1), 0)
                self.__oldmouseMovePos_y = max(min(event.y()//self.settings.get_cellsize(), self.settings.get_gridheight()-1), 0)
                self.ceausi_grid.grid[max(min(event.x()//self.settings.get_cellsize(), self.settings.get_gridwidth()-1), 0)][max(min(event.y()//self.settings.get_cellsize(), self.settings.get_gridheight()-1), 0)] = 1 ^ self.ceausi_grid.grid[max(min(event.x()//self.settings.get_cellsize(), self.settings.get_gridheight()-1), 0)][max(min(event.y()//self.settings.get_cellsize(), self.settings.get_gridwidth()-1), 0)]
                self.update()
        elif self.settings.get_currentmode() == self.settings.get_selectionmodeID():
            if event.buttons() == Qt.LeftButton:
                self.__drawSquareMode = 1
                self.__begSquare = [max(min(event.x()//self.settings.get_cellsize(), self.settings.get_gridwidth()-1), 0), max(min(event.y()//self.settings.get_cellsize(), self.settings.get_gridheight()-1), 0)]
    def mouseReleaseEvent(self, event):
        if self.settings.get_currentmode() == self.settings.get_drawmodeID():
            if self.__drawSquareMode == 1:
                self.__endSquare = [max(min(event.x()//self.settings.get_cellsize(), self.settings.get_gridwidth()-1), 0), max(min(event.y()//self.settings.get_cellsize(), self.settings.get_gridheight()-1), 0)]
                #print('Drawing Square between', self.__begSquare, self.__endSquare)
                if self.__begSquare != [-1,-1] and self.__endSquare != [-1,-1]:
                    self.ceausi_grid.drawSquare(self.__begSquare, self.__endSquare, 1, drawplain=False)
                    self.__begSquare, self.__endSquare = [-1,-1], [-1,-1]
                self.__drawSquareMode = 0
                self.update()
        elif self.settings.get_currentmode() == self.settings.get_selectionmodeID():
            self.__endSquare = [max(min(event.x()//self.settings.get_cellsize(), self.settings.get_gridwidth()-1), 0), max(min(event.y()//self.settings.get_cellsize(), self.settings.get_gridheight()-1), 0)]
            print('Selecting zone between', self.__begSquare, self.__endSquare)
            if self.__begSquare != [-1,-1] and self.__endSquare != [-1,-1]:
                self.ceausi_overlay_grid.drawSquare(self.__begSquare, self.__endSquare, 1, drawplain=True)
                self.__begSquare, self.__endSquare = [-1,-1], [-1,-1]
            self.update()

    def mouseMoveEvent(self, event):
        if self.settings.get_currentmode() == self.settings.get_drawmodeID():
            if event.buttons() == Qt.LeftButton:
                if self.__oldmouseMovePos_x != max(min(event.x()//self.settings.get_cellsize(), self.settings.get_gridwidth()-1), 0) or self.__oldmouseMovePos_y != max(min(event.y()//self.settings.get_cellsize(), self.settings.get_gridheight()-1), 0) :
                    self.ceausi_grid.grid[max(min(event.x()//self.settings.get_cellsize(), self.settings.get_gridwidth()-1), 0)][max(min(event.y()//self.settings.get_cellsize(), self.settings.get_gridheight()-1), 0)] = 1 ^ self.ceausi_grid.grid[max(min(event.x()//self.settings.get_cellsize(), self.settings.get_gridwidth()-1), 0)][max(min(event.y()//self.settings.get_cellsize(), self.settings.get_gridheight()-1), 0)]
                    self.update()
                self.__oldmouseMovePos_x = max(min(event.x()//self.settings.get_cellsize(), self.settings.get_gridwidth()-1), 0)
                self.__oldmouseMovePos_y = max(min(event.y()//self.settings.get_cellsize(), self.settings.get_gridheight()-1), 0)
            elif event.buttons() == Qt.RightButton:
                pass
        elif self.settings.get_currentmode() == self.settings.get_selectionmodeID():
            pass


    # *------------------------openFileNameDialog------------------------------*

    def openGridFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open Grid File", "","Ceausi Grid Files (*.casgrid)", options=options)
        if fileName:
            errcode = self.ceausi_grid.loadGridFromFile(fileName)
            if errcode == 0:
                return -1
            else :
                return errcode
        else:
            return -1

    def saveGridFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Grid","","Ceausi Grid Files (*.casgrid)", options=options)
        if fileName:
            errcode = self.ceausi_grid.saveGridToFile(fileName)
            if errcode == 0:
                return -1
            else :
                return errcode
        else:
            return -1

    def openElemFileDialog(self):
        self.ceausi_element = CeausiElement()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Open Element File", "","Ceausi Element Files (*.caselem)", options=options)
        if fileName:
            errcode = self.ceausi_element.loadElemFromFile(fileName)
            if errcode == 0:
                return 0
            else :
                return errcode
        else:
            return -1

    def saveElemFileDialog(self):
        self.ceausi_element = CeausiElement()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Element","","Ceausi Element Files (*.caselem)", options=options)
        if fileName:
            errcode = self.ceausi_element.saveElemToFile(fileName)
            if errcode == 0:
                return 0
            else :
                return errcode
        else:
            return -1


    # *----------------------------GET--SET------------------------------------*

    def get_grid (self):
        return self.ceausi_grid.grid

    def set_grid (self, grid):
        self.ceausi_grid.grid = grid

    def get_mode (self):
        return self.mode

    def set_mode (self, mode):
        self.mode = max(0, min(mode, 1))

    def get_settings (self):
        return self.settings

    def set_settings (self, settings):
        self.settings = settings
