#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimlator -> CellularAutomataSimulatorApp

Author: Remi GASCOU
Last edited: November 2018
"""

import os, sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib.ui import *
from lib.core import *
from lib.core.Settings import *

class CellularAutomataSimulatorApp(QMainWindow):
    """docstring for CellularAutomataSimulatorApp."""
    def __init__(self, gridwidth=10, gridheight=10, parent=None):
        super(CellularAutomataSimulatorApp, self).__init__()
        self.title        = CellularAutomataSimulatorAppInfos.get_name() + " - " + CellularAutomataSimulatorAppInfos.get_versiontag()
        self.settings     = Settings()
        self.settings.set_gridwidth(gridwidth)
        self.settings.set_gridheight(gridheight)

        self.margin_left  = 200
        self.margin_top   = 200
        self.width        = self.settings.get_gridwidth()*self.settings.get_cellsize()
        self.height       = self.settings.get_gridheight()*self.settings.get_cellsize()+21
        self.timer_state  = False

        self._initUI()
        self._initMenus()
        self.timer  = QTimer()
        self.timer.timeout.connect(self.timerTimeoutEvent)
        self.__curentIcoId = 0

    def timerTimeoutEvent(self):
        self.__curentIcoId = (self.__curentIcoId + 1)%4
        self.setWindowIcon(QIcon('lib/meta/anim_ico_' + str(self.__curentIcoId) + '.png'))
        self.ceausi_canvas.updateGrid()

    def _initUI(self):
        self.setWindowTitle(self.title + " - [PAUSED]")
        self.setWindowIcon(QIcon('lib/meta/ico.png'))
        self.setGeometry(self.margin_left, self.margin_top, self.width, self.height)
        self.setFixedSize(self.size())
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ceausi_canvas = CeausiCanvas(self.settings)
        self.setCentralWidget(self.ceausi_canvas)
        self.show()

    def _initMenus(self):
        mainMenu        = self.menuBar()
        appMenu         = mainMenu.addMenu('Ceausi')
        editMenu        = mainMenu.addMenu('Edit')
        simulationMenu  = mainMenu.addMenu('Simulation')
        settingsMenu    = mainMenu.addMenu('Settings')
        helpMenu        = mainMenu.addMenu('Help')

        #appMenu buttons
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        appMenu.addAction(exitButton)

        #fileMenu buttons
        #openFileButton = QAction('Open File', self)
        #openFileButton.setShortcut('Ctrl + O')
        #openFileButton.triggered.connect(self.start_OpenFileWindow)
        #fileMenu.addAction(openFileButton)

        #editMenu buttons

        #modeMenu buttons
        modeMenu = editMenu.addMenu('Mode')
        modeAG = QActionGroup(modeMenu, exclusive=True)
        #
        drawModeButton = modeAG.addAction(QAction('Draw Mode', self, checked=True, checkable=True))
        drawModeButton.changed.connect(self.switchToDrawMode)
        drawModeButton.toggle()
        modeMenu.addAction(drawModeButton)
        #
        selectionModeButton = modeAG.addAction(QAction('Selection Mode', self, checkable=True))
        selectionModeButton.changed.connect(self.switchToSelectionMode)
        modeAG.addAction(selectionModeButton)
        modeMenu.addAction(selectionModeButton)



        loadxorElemButton = QAction('Load XOR element', self)
        loadxorElemButton.triggered.connect(self.start_openElemFileWindow)
        editMenu.addAction(loadxorElemButton)
        loadElemButton = QAction('Load element', self)
        loadElemButton.triggered.connect(self.start_openElemFileWindow)
        editMenu.addAction(loadElemButton)
        saveElemButton = QAction('Save element', self)
        saveElemButton.triggered.connect(self.start_openElemFileWindow)
        editMenu.addAction(saveElemButton)
        editMenu.addSeparator()
        copyZoneButton = QAction('Copy', self)
        copyZoneButton.setShortcut('Ctrl + C')
        copyZoneButton.triggered.connect(self.start_none)
        editMenu.addAction(copyZoneButton)
        pasteZoneButton = QAction('Paste', self)
        pasteZoneButton.setShortcut('Ctrl + V')
        pasteZoneButton.triggered.connect(self.start_none)
        editMenu.addAction(pasteZoneButton)
        cutZoneButton = QAction('Cut', self)
        cutZoneButton.setShortcut('Ctrl + X')
        cutZoneButton.triggered.connect(self.start_none)
        editMenu.addAction(cutZoneButton)
        clearZoneButton = QAction('Clear', self)
        clearZoneButton.setShortcut('Ctrl + Space')
        clearZoneButton.triggered.connect(self.start_none)
        editMenu.addAction(clearZoneButton)

        #simulationMenu buttons
        rulesButton = QAction('Manage rules', self)
        rulesButton.triggered.connect(self.start_RulesWindow)
        simulationMenu.addAction(rulesButton)
        simulationMenu.addSeparator()
        openGridFileButton = QAction('Open Grid File', self)
        openGridFileButton.triggered.connect(self.start_openGridFileWindow)
        simulationMenu.addAction(openGridFileButton)
        saveGridFileButton = QAction('Save Grid File', self)
        saveGridFileButton.triggered.connect(self.start_saveGridFileWindow)
        simulationMenu.addAction(saveGridFileButton)

        #settingsMenu buttons
        settingsButton = QAction('Settings', self)
        settingsButton.triggered.connect(self.start_SettingsWindow)
        settingsMenu.addAction(settingsButton)

        #helpMenu buttons
        aboutButton = QAction('About', self)
        aboutButton.triggered.connect(self.start_AboutWindow)
        helpMenu.addAction(aboutButton)
        # helpMenu.addSeparator()
        # debugButton = QAction('Debug', self)
        # debugButton.triggered.connect(self.start_DebugWindow)
        # helpMenu.addAction(debugButton)
        # testButton = QAction('Test checkbox', self, checkable=True)
        # testButton.changed.connect(self.start_none)
        # helpMenu.addAction(testButton)

    def _updateUI(self):
        self.timer.stop()
        self.timer_state = False
        self.setWindowIcon(QIcon('lib/meta/ico.png'))
        self.width  = self.gridwidth*self.settings.get_cellsize()
        self.height = self.gridheight*self.settings.get_cellsize()-4
        self.setGeometry(self.margin_left, self.margin_top, self.width, self.height)
        self.setFixedSize(self.size())
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ceausi_canvas  = CeausiCanvas(self.settings.get_cellsize(), self.gridwidth, self.gridheight)
        self.setCentralWidget(self.ceausi_canvas)
        self.timer          = QTimer()
        self.timer.timeout.connect(self.ceausi_canvas.updateGrid)
        self.show()

    def keyPressEvent(self, event):
        if   event.key() == Qt.Key_Space:
            if self.timer_state == True :
                self.timer_stop()
            else :
                self.timer_start()
        elif event.key() == Qt.Key_N and self.timer_state == False:
            self.timerTimeoutEvent()
        elif event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_R:
            self.ceausi_canvas.regen()
        elif event.key() == Qt.Key_C:
            self.ceausi_canvas.cleargrid()

    def timer_stop(self):
        self.timer_state = False
        self.timer.stop()
        self.__curentIcoId = 0
        self.setWindowIcon(QIcon('lib/meta/ico.png'))
        self.setWindowTitle(self.title +" - [PAUSED]")

    def timer_start(self):
        self.timer_state = True
        self.timer.start(self.settings.get_timerperiod())
        self.setWindowTitle(self.title)

# *------------------------------Windows Handlers----------------------------- *

    def errorHandler(f_in, f_win, errortitle, errormessage):
        errcode = f_in()
        if (errcode == 0):
            f_win()
        else:
            e = ErrorWindow("Error", "", errcode)

    def start_none(self):
        print("start_none")
        pass

    def switchToDrawMode(self):
        #self.timer_stop()
        # print("switchToDrawMode : ", self.settings.get_currentmode(), end=" -> ")
        self.settings.set_currentmode(self.settings.get_drawmodeID())
        # print(self.settings.get_currentmode())

    def switchToSelectionMode(self):
        #self.timer_stop()
        # print("switchToSelectionMode : ", self.settings.get_currentmode(), end=" -> ")
        self.settings.set_currentmode(self.settings.get_selectionmodeID())
        # print(self.settings.get_currentmode())

    def start_openElemFileWindow(self):
        self.timer_stop()
        errorHandler(
            self.ceausi_canvas.openElemFileDialog,
            self.ceausi_canvas.update,
            "FileError",
            "Could not open file."
        )


    def start_SettingsWindow(self):
        self.wSettingsWindow = SettingsWindow(self)
        self.wSettingsWindow.show()

    def start_openGridFileWindow(self):
        self.timer_stop()
        self.ceausi_canvas.openGridFileDialog()
        self.ceausi_canvas.update()

    def start_saveGridFileWindow(self):
        self.timer_stop()
        self.ceausi_canvas.saveGridFileDialog()

    def start_RulesWindow(self):
        self.wRulesWindow = RulesWindow(self)
        self.wRulesWindow.show()

    def start_AboutWindow(self):
        self.wAboutWindow = AboutWindow(self)
        self.wAboutWindow.show()

    def start_DebugWindow(self):
        self.wDebugWindow = DebugWindow(self)
        self.wDebugWindow.show()

# *----------------------------------Get Set---------------------------------- *
    def get_cellsize (self):
        return self.settings.get_cellsize()

    def set_cellsize (self, cellsize):
        self.settings.set_cellsize(max(0,cellsize))
        self.ceausi_canvas.set_cellsize(self.settings.get_cellsize())
        self._updateUI()

    def get_gridwidth (self):
        return self.gridwidth

    def set_gridwidth (self, gridwidth):
        self.gridwidth = max(0,gridwidth)
        self.ceausi_canvas.set_gridwidth(self.gridwidth)
        self._updateUI()

    def get_gridheight (self):
        return self.gridheight

    def set_gridheight (self, gridheight):
        self.gridheight = max(0,gridheight)
        self.ceausi_canvas.set_gridheight(self.gridheight)
        self._updateUI()


if __name__ == """__main__""":
    app = QApplication(sys.argv)
    ex = CellularAutomataSimulatorApp(int(76*1.25),int(40*1.25))
