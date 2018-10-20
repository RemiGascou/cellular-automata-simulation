from numpy import array, zeros
from random import choice


class Conway(object):
    """docstring for Conway."""
    def __init__(self, arg):
        super(Conway, self).__init__()
        self.grid = grid

    def getNeighbours(self, x, y):
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
        neighbours.update({(x,y):2}) # Add the value of the cell for which we look the neighbours, make sure not to use the value 2 for either valueOn and valueOff as it's used here
        return neighbours

    def countNeighbours(self.grid, x, y, valueOn, valueOff):
        """
            Function that, for a given self.grid and a given cell, identified with its coordinates x and y, return the number of cells in its neighbourhood that are on and the number that are off
            Parameters :
                - self.grid : a n x m array with the values of each cell, dead or alive
                - x : the coordinate of the cell on the x-axis
                - y : the coordinate of the cell on the y-axis
                - valueOn : the value that code the fact that a cell is on
                - valueOff : the value that code the fact that a cell is off
            Return :
                - numberOn, numberOff : the number of cells that are on and off in the neighbourhood
        """
        numberOn, numberOff = 0, 0
        neighbours = getNeighbours(self.grid, x, y)
        for key in neighbours.keys(): # we go through all the keys in the dict, so all the coordinates of the neighbours
            if(neighbours[key] == valueOn):
                numberOn += 1
            elif(neighbours[key] == valueOff):
                numberOff += 1
        return numberOn, numberOff

    def applyRules(self, valueOn, valueOff):
        """
            Function that, for a given self.grid, apply the rules of the game (see below for the detail)
            Parameters :
                - self.grid : a n x m array with the values of each cell, dead or alive
                - valueOn : the value that code the fact that a cell is on
                - valueOff : the value that code the fact that a cell is off
            Return :
                - nextself.grid : the self.grid updated with the rules of the game (see below for the detail)
            Note : the rules are the following
                1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
                2. Any live cell with two or three live neighbours lives on to the next generation.
                3. Any live cell with more than three live neighbours dies, as if by overpopulation.
                4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        nextself.grid = [[valueOff for y in range(len(self.grid[0]))] for x in range(len(self.grid))]
        for x in range(len(self.grid)): # we go through all the point on the x-axis
            for y in range(len(self.grid[0])): # we go through all the point on the y-axis
                numberOn, numberOff = countNeighbours(self.grid, x, y, valueOn, valueOff)
                if(self.grid[x][y] == valueOn): # For the rules 1, 2 and 3
                    if(numberOn < 2): # For the rule 1
                        nextself.grid[x][y] = valueOff
                    elif(numberOn == 2 or numberOn == 3): # For the rule 2
                        nextself.grid[x][y] = valueOn
                    elif(numberOn > 3): # For the rule 3
                        nextself.grid[x][y] = valueOff
                elif(self.grid[x][y] == valueOff and numberOn == 3): # For the rule 4
                    nextself.grid[x][y] = valueOn
        return(nextself.grid)

    def showgrid(self):
        """
            Useful fonction to show the self.grid, not absolutely necessary, can be not used
        """
        print(array(self.grid))

    def generateRandomgrid(xSize, ySize, valueOn, valueOff):
        """
            Function that generate randomly a self.grid
            Parameters :
                - xSize : the size of the self.grid on the x-axis
                - ySize : the size of the self.grid on the x-axis
                - valueOn : the value that code the fact that a cell is on
                - valueOff : the value that code the fact that a cell is off
            Return :
                - self.grid : the self.grid generated randomly
        """
        self.grid = zeros((xSize, ySize), dtype=int)
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                self.grid[x][y] = choice([valueOn, valueOff]) # for each cell, we choose randomly a value between valueOn and valueOff
        return self.grid


if __name__ == '__main__':
    main()

    # Values that code the fact that the cells are on and off (respectively alive and dead)
    valueOn = 2
    valueOff = 0

    # There are two ways to create a self.grid :
    # 1- Manually by creating a list of lists containing the same number of elements each time, where each element can be valueOn or valueOff (see above for the defined values
    # example of a 3x3 manually definded self.grid : self.grid = [[valueOn,valueOn,valueOff],[valueOn,valueOff,valueOn],[valueOff,valueOn,valueOff]]
    # 2- With the function generateRandomself.grid(xSize, ySize, valueOn, valueOff) (see above for the definition of each parameter
    # example of a 4x6 randomly generated self.grid : self.grid = generateRandomself.grid(4, 6, valueOn, valueOff)

    # Generation of the self.grid
    grid = generateRandomgrid(4, 6, valueOn, valueOff)

    # Number of turns
    turns = 20
    showgrid(grid) # Show the initial self.grid

    for i in range(turns):
        print('----- Step',i+1,'-----')
        grid = applyRules(grid, valueOn, valueOff)
        showgrid(grid)
