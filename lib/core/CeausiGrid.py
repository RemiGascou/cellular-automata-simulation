#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CellularAutomataSimlator -> CeausiGrid

Author: Remi GASCOU
Last edited: November 2018
"""

import json
from numpy import array, zeros
from random import choice

class CeausiGrid(object):
    def __init__(self, settings, parent=None):
        super(CeausiGrid, self).__init__()
        self.settings   = settings
        self.grid       = []
        self.cleargrid()

    def regen(self):
        self.grid       = self._generateRandomgrid()

    def cleargrid(self):
        self.grid.clear()
        for _ in range(self.settings.get_gridwidth()):
            self.grid.append([self.settings.get_valueCellOff() for k in range(self.settings.get_gridheight())])
        self.applyRules()

    def updateGrid(self):
        if len(self.grid) != 0:
            self.applyRules()

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
        neighbours.update({(x,y):2}) # Add the value of the cell for which we look the neighbours, make sure not to use the value 2 for either self.settings.get_valueCellOn() and self.settings.get_valueCellOff() as it's used here
        return neighbours

    def _countNeighbours(self, x, y):
        """
            Function that, for a given self.grid and a given cell, identified with its coordinates x and y, return the number of cells in its neighbourhood that are on and the number that are off
            Parameters :
                - self.grid : a n x m array with the values of each cell, dead or alive
                - x : the coordinate of the cell on the x-axis
                - y : the coordinate of the cell on the y-axis
                - self.settings.get_valueCellOn() : the value that code the fact that a cell is on
                - self.settings.get_valueCellOff() : the value that code the fact that a cell is off
            Return :
                - numberOn, numberOff : the number of cells that are on and off in the neighbourhood
        """
        numberOn, numberOff = 0, 0
        neighbours = self._getNeighbours(x, y)
        for key in neighbours.keys(): # we go through all the keys in the dict, so all the coordinates of the neighbours
            if(neighbours[key] == self.settings.get_valueCellOn()):
                numberOn += 1
            elif(neighbours[key] == self.settings.get_valueCellOff()):
                numberOff += 1
        return numberOn, numberOff

    def applyRules(self):
        """
            Function that, for a given grid, apply the rules of the game (see below for the detail)
            Parameters :
                - self.grid : a n x m array with the values of each cell, dead or alive
                - self.settings.get_valueCellOn() : the value that code the fact that a cell is on
                - self.settings.get_valueCellOff() : the value that code the fact that a cell is off
            Return :
                - nextgrid : the self.grid updated with the rules of the game (see below for the detail)
            Note : the rules are the following
                1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
                2. Any live cell with two or three live neighbours lives on to the next generation.
                3. Any live cell with more than three live neighbours dies, as if by overpopulation.
                4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        nextgrid = [[self.settings.get_valueCellOff() for y in range(len(self.grid[0]))] for x in range(len(self.grid))]
        for x in range(len(self.grid)): # we go through all the point on the x-axis
            for y in range(len(self.grid[0])): # we go through all the point on the y-axis
                numberOn, numberOff = self._countNeighbours(x, y)
                if(self.grid[x][y] == self.settings.get_valueCellOn()): # For the rules 1, 2 and 3
                    if(numberOn < 2): # For the rule 1
                        nextgrid[x][y] = self.settings.get_valueCellOff()
                    elif(numberOn == 2 or numberOn == 3): # For the rule 2
                        nextgrid[x][y] = self.settings.get_valueCellOn()
                    elif(numberOn > 3): # For the rule 3
                        nextgrid[x][y] = self.settings.get_valueCellOff()
                elif(self.grid[x][y] == self.settings.get_valueCellOff() and numberOn == 3): # For the rule 4
                    nextgrid[x][y] = self.settings.get_valueCellOn()
        self.grid = nextgrid

    def _generateRandomgrid(self):
        self.grid = [[choice([self.settings.get_valueCellOn(), self.settings.get_valueCellOff()]) for yk in range(self.settings.get_gridheight())] for xk in range(self.settings.get_gridwidth())]
        return self.grid

# *------------------------------- Utils --------------------------------------*

    def drawSquare(self, nodeA, nodeB, value, drawplain=False):
        if nodeA != nodeB and nodeA[0] != -1 and nodeA[1] != -1 and nodeB[0] != -1 and nodeB[1] != -1:
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


# *------------------------------- Files --------------------------------------*


    def loadGridFromFile(self, path):
        #print("loadGridFromFile :", path)
        f = open(path,'r')
        jsondata = ''.join([e for e in f.readlines() if type(e) == str])
        f.close()
        d_in = json.loads(jsondata)
        self.settings.set_valueCellOff(d_in['grid_data']['valueOff'])
        self.settings.set_valueCellOn(d_in['grid_data']['valueOn'])
        self.settings.set_gridheight(len(self.grid))
        self.settings.set_gridwidth(len(self.grid[0]))
        self.grid       = d_in['grid_data']['grid'].copy()


    def saveGridToFile(self, path):
        #print("saveGridToFile :", path)
        if not path.endswith(".casgrid"):
            path += ".casgrid"
        jsondata = """{\n\t"grid_data": {\n\t\t"name": "Example Grid",\n\t\t"valueOff": """ + str(self.settings.get_valueCellOff()) + """,\n\t\t"valueOn": """ + str(self.settings.get_valueCellOn()) + """,\n\t\t"grid":""" + str(self.grid) + """\n\t}\n}"""
        f = open(path,'w+')
        f.write(jsondata)
        f.close()



    # *----------------------------GET--SET------------------------------------*

    def get_grid (self):
        return self.grid

    def set_grid (self, grid):
        self.grid = grid
