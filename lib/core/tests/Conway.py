from numpy import array, zeros
from random import choice


class ConwayCanvas(QWidget):
    def __init__(self, height, width, parent=None):
        super(ConwayCanvas, self).__init__()
        self.height         = height
        self.width          = width
        self.gridheight     = 10
        self.gridwidth      = 10

        self.colorOn    = [0,0,0]
        self.colorOff   = [255,255,255]

        self.valueOn    = 0
        self.valueOff   = 1
        self.grid       = self._generateRandomgrid(self.gridheight, self.gridwidth)
        self.initUI()

    def initUI(self):
        self.qp = QPainter()
        self.qp.begin(self)
        self.qp.end()

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
        if(x == 0):
            if(y == 0): # Upper left corner
                neighbours = {
                (x,y+1):self.grid[x][y+1],
                (x+1,y):self.grid[x+1][y],
                (x+1,y+1):self.grid[x+1][y+1]
                }
            elif(y == len(self.grid[0])-1): # Upper right corner
                neighbours = {
                (x,y-1):self.grid[x][y-1],
                (x+1,y):self.grid[x+1][y],
                (x+1,y-1):self.grid[x+1][y-1]
                }
            else: # Upper border
                neighbours = {
                (x,y-1):self.grid[x][y-1],
                (x,y+1):self.grid[x][y+1],
                (x+1,y-1):self.grid[x+1][y-1],
                (x+1,y):self.grid[x+1][y],
                (x+1,y+1):self.grid[x+1][y-1]
                }
        elif(x == len(self.grid)-1):
            if(y == 0): # Left down corner
                neighbours = {
                (x-1,y):self.grid[x-1][y],
                (x,y+1):self.grid[x][y+1],
                (x-1,y+1):self.grid[x-1][y+1]
                }
            elif(y == len(self.grid[0])-1): # Right down corner
                neighbours = {
                (x,y-1):self.grid[x][y-1],
                (x-1,y):self.grid[x-1][y],
                (x-1,y-1):self.grid[x-1][y-1]
                }
            else: # Down border
                neighbours = {
                (x,y+1):self.grid[x][y+1],
                (x,y-1):self.grid[x][y-1],
                (x-1,y-1):self.grid[x-1][y-1],
                (x-1,y):self.grid[x-1][y],
                (x-1,y+1):self.grid[x-1][y+1]
                }
        else:
            if(y == 0): # Left border
                neighbours = {
                (x-1,y):self.grid[x-1][y],
                (x+1,y):self.grid[x+1][y],
                (x-1,y+1):self.grid[x-1][y+1],
                (x,y+1):self.grid[x][y+1],
                (x+1,y+1):self.grid[x+1][y+1]
                }
            elif(y == len(self.grid[0])-1): # Right border
                neighbours = {
                (x-1,y):self.grid[x-1][y],
                (x+1,y):self.grid[x+1][y],
                (x-1,y-1):self.grid[x-1][y-1],
                (x,y-1):self.grid[x][y-1],
                (x+1,y-1):self.grid[x+1][y-1]
                }
            else: # Middle
                neighbours = {
                (x-1,y-1):self.grid[x-1][y-1],
                (x-1,y):self.grid[x-1][y],
                (x-1,y+1):self.grid[x-1][y+1],
                (x,y-1):self.grid[x][y-1],
                (x,y+1):self.grid[x][y+1],
                (x+1,y-1):self.grid[x+1][y-1],
                (x+1,y):self.grid[x+1][y],
                (x+1,y+1):self.grid[x+1][y+1]
                }
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
        neighbours = self.getNeighbours(self.grid, x, y)
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
                numberOn, numberOff = self.countNeighbours(self.grid, x, y, self.valueOn, self.valueOff)
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

    def printgrid(self):
        """
            Useful fonction to show the self.grid, not absolutely necessary, can be not used
        """
        print(array(self.grid))

    def _generateRandomgrid(self, xSize, ySize):
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
        self.grid = zeros((xSize, ySize), dtype=int)
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                self.grid[x][y] = choice([self.valueOn, self.valueOff]) # for each cell, we choose randomly a value between self.valueOn and self.valueOff
        return self.grid

    def update(self):
        if len(grid) != 0:
            self.applyRules()
            self.qp.begin(self)
            for xk in range(len(self.grid)):
                for yk in range(len(self.grid[0])):
                    if grid[xk][yk] == self.valueOn:
                        self.qp.setBrush(QColor(self.colorOn[0], self.colorOn[1], self.colorOn[2]))
                    else :
                        self.qp.setBrush(QColor(self.colorOff[0], self.colorOff[1], self.colorOff[2]))
                    self.qp.drawRect(10*xk, 10*yk, 10*(xk+1), 10*(yk+1))
            self.qp.end()

    def update_event(self):
        self.update()


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


if __name__ == '__main__':
    pass
