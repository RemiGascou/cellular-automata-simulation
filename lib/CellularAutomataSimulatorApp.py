# -*- coding: utf-8 -*-

import os, sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib.ui import *
from lib.core import *

class CellularAutomataSimulatorApp(QMainWindow):
    """docstring for CellularAutomataSimulatorApp."""
    def __init__(self, gridwidth=10, gridheight=10, parent=None):
        super(CellularAutomataSimulatorApp, self).__init__()
        self.title        = CellularAutomataSimulatorAppInfos.get_name() + " - " + CellularAutomataSimulatorAppInfos.get_versiontag()
        self.gridwidth    = gridwidth
        self.gridheight   = gridheight
        self.cellsize     = 25
        self.margin_left  = 200
        self.margin_top   = 200
        self.width        = self.gridwidth*self.cellsize
        self.height       = self.gridheight*self.cellsize-4
        self.timer_period = 125
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
        self.ceausi_canvas = CeausiCanvas(self.cellsize, self.gridwidth, self.gridheight)
        self.setCentralWidget(self.ceausi_canvas)
        self.show()

    def _initMenus(self):
        mainMenu        = self.menuBar()
        appMenu         = mainMenu.addMenu('Ceausi')
        #fileMenu        = mainMenu.addMenu('File')
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
        settingsButton.triggered.connect(self.close)
        settingsMenu.addAction(settingsButton)

        #helpMenu buttons
        aboutButton = QAction('About', self)
        aboutButton.triggered.connect(self.start_AboutWindow)
        helpMenu.addAction(aboutButton)
        helpMenu.addSeparator()
        debugButton = QAction('Debug', self)
        debugButton.triggered.connect(self.start_DebugWindow)
        helpMenu.addAction(debugButton)

    def _updateUI(self):
        self.timer.stop()
        self.timer_state = False
        self.setWindowIcon(QIcon('lib/meta/ico.png'))
        self.width  = self.gridwidth*self.cellsize
        self.height = self.gridheight*self.cellsize-4
        self.setGeometry(self.margin_left, self.margin_top, self.width, self.height)
        self.setFixedSize(self.size())
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ceausi_canvas  = CeausiCanvas(self.cellsize, self.gridwidth, self.gridheight)
        self.setCentralWidget(self.ceausi_canvas)
        self.timer          = QTimer()
        self.timer.timeout.connect(self.ceausi_canvas.updateGrid)
        self.show()

    def keyPressEvent(self, event):
        if   event.key() == Qt.Key_Space:
            if self.timer_state == True :
                self.timer_state = False
                self.timer.stop()
                self.__curentIcoId = 0
                self.setWindowTitle(self.title +" - [PAUSED]")
            else :
                self.timer_state = True
                self.timer.start(self.timer_period)
                self.setWindowTitle(self.title)
        elif event.key() == Qt.Key_N:
            self.timerTimeoutEvent()
        elif event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_R:
            self.ceausi_canvas.regen()
        elif event.key() == Qt.Key_C:
            self.ceausi_canvas.cleargrid()

# *------------------------------Windows Handlers----------------------------- *

    def start_openGridFileWindow(self):
        self.timer.stop()
        self.timer_state = False
        self.setWindowTitle(self.title + " - [PAUSED]")
        self.setWindowIcon(QIcon('lib/meta/ico.png'))
        self.ceausi_canvas.openGridFileDialog()
        self.ceausi_canvas.update()

    def start_saveGridFileWindow(self):
        self.timer.stop()
        self.timer_state = False
        self.setWindowTitle(self.title + " - [PAUSED]")
        self.setWindowIcon(QIcon('lib/meta/ico.png'))
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
        return self.cellsize

    def set_cellsize (self, cellsize):
        self.cellsize = max(0,cellsize)
        self.ceausi_canvas.set_cellsize(self.cellsize)
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
    ex = CellularAutomataSimulatorApp(38,20) #76,40
    sys.exit(app.exec_())
