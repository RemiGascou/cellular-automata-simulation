#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimulatorApp -> SettingsWindow

Author: Remi GASCOU
Last edited: October 2018
"""

import sys
from lib.core.Settings import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class SettingsWindow(QWidget):
    def __init__(self, settings:Settings, parent=None):
        print("[LOG] Parent of SettingsWindow", parent)
        super(SettingsWindow, self).__init__()
        self.title = 'Settings'
        self.left   = 100
        self.top    = 100
        self.width  = 600
        self.height = 500
        self.settings = settings
        self.tabs = []
        self._initUI()
        self.show()

    def _initUI(self):
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)  #Kill application on close
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('lib/meta/ico.png'))
        #
        layout = QVBoxLayout(self)
        self.tabsWidget = QTabWidget()
        #Load Stylesheet from "TabsManager.css"
        f = open("lib/ui/stylesheets/SettingsWindow.css",'r')
        stylesheet = "".join(f.readlines())
        f.close()
        #EndLoad
        self.tabsWidget.setStyleSheet(stylesheet)
        self.tabsBarWidget = self.tabsWidget.tabBar()
        self.tabsBarWidget.setTabsClosable(False)

        #
        self.__init_generalsettings_tab()
        self.__init_drawsettings_tab()
        self.__init_colorsettings_tab()
        #
        self._updatetabs()
        layout.addWidget(self.tabsWidget)
        self.setLayout(layout)


    def __init_generalsettings_tab(self, title = "General settings"):
        self.generalsettings_tab = QWidget()
        self.generalsettings_tab.layout = QGridLayout(self.generalsettings_tab)
        self.generalsettings_tab.setLayout(self.generalsettings_tab.layout)
        tabdata = {"object": self.generalsettings_tab, "title": title}
        self.tabs.append(tabdata)

    def __init_drawsettings_tab(self, title = "Draw settings"):
        self.drawsettings_tab = QWidget()
        self.drawsettings_tab.layout = QGridLayout(self.drawsettings_tab)
        self.drawsettings_tab.setLayout(self.drawsettings_tab.layout)
        tabdata = {"object": self.drawsettings_tab, "title": title}
        self.tabs.append(tabdata)

    def __init_colorsettings_tab(self, title = "Colors settings"):
        self.colorsettings_tab = QWidget()
        self.colorsettings_tab.layout = QGridLayout(self.colorsettings_tab)
        self.colorsettings_tab.setLayout(self.colorsettings_tab.layout)
        tabdata = {"object": self.colorsettings_tab, "title": title}
        self.tabs.append(tabdata)

    def _updatetabs(self):
        self.tabsWidget.clear()
        for tab in self.tabs:
            self.tabsWidget.addTab(tab["object"],tab["title"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SettingsWindow()
    sys.exit(app.exec_())
