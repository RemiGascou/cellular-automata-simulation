#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import *
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import *
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        
        self.grid = []
        self.gen_ran_grid()
        self.initUI()

    def gen_ran_grid(self):
        self.grid.clear()
        for xk in range(12):
            buffer = []
            for yk in range(12):
                buffer.append(int(2*random()))
            self.grid.append(buffer)

    def initUI(self):
        self.setGeometry(0,0,len(self.grid)*20, len(self.grid[0])*20)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):
        qp = QPainter(self)
        self.gen_ran_grid()
        self.drawRectangles(qp)
    
    def uev(self):
        qp = QPainter(self)
        self.gen_ran_grid()
        self.drawRectangles(qp)

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        qp.setPen(col)
        for yk in range(len(self.grid)):
            for xk in range(len(self.grid[0])):
                if self.grid[xk][yk] == 1:
                    qp.setBrush(QColor(0,0,0))
                else :
                    qp.setBrush(QColor(190,190,190))
                qp.drawRect(xk*20,yk*20, 20, 20)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    timer = QTimer()
    timer.timeout.connect(ex.update)
    timer.start(250)
    sys.exit(app.exec_())
