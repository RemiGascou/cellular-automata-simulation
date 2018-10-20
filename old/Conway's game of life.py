from numpy import array, zeros
from random import choice

def getNeighbours(grid, x, y):
    """
        Function that, for a given grid and a given cell, identified with its coordinates x and y, return the coordinates and values of its neighbours
        Parameters :
            - grid : a n x m array with the values of each cell, dead or alive
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
            (x,y+1):grid[x][y+1],
            (x+1,y):grid[x+1][y],
            (x+1,y+1):grid[x+1][y+1]
            }
        elif(y == len(grid[0])-1): # Upper right corner
            neighbours = {
            (x,y-1):grid[x][y-1],
            (x+1,y):grid[x+1][y],
            (x+1,y-1):grid[x+1][y-1]
            }
        else: # Upper border
            neighbours = {
            (x,y-1):grid[x][y-1],
            (x,y+1):grid[x][y+1],
            (x+1,y-1):grid[x+1][y-1],
            (x+1,y):grid[x+1][y],
            (x+1,y+1):grid[x+1][y-1]
            }
    elif(x == len(grid)-1):
        if(y == 0): # Left down corner
            neighbours = {
            (x-1,y):grid[x-1][y],
            (x,y+1):grid[x][y+1],
            (x-1,y+1):grid[x-1][y+1]
            }
        elif(y == len(grid[0])-1): # Right down corner
            neighbours = {
            (x,y-1):grid[x][y-1],
            (x-1,y):grid[x-1][y],
            (x-1,y-1):grid[x-1][y-1]
            }
        else: # Down border
            neighbours = {
            (x,y+1):grid[x][y+1],
            (x,y-1):grid[x][y-1],
            (x-1,y-1):grid[x-1][y-1],
            (x-1,y):grid[x-1][y],
            (x-1,y+1):grid[x-1][y+1]
            }
    else:
        if(y == 0): # Left border
            neighbours = {
            (x-1,y):grid[x-1][y],
            (x+1,y):grid[x+1][y],
            (x-1,y+1):grid[x-1][y+1],
            (x,y+1):grid[x][y+1],
            (x+1,y+1):grid[x+1][y+1]
            }
        elif(y == len(grid[0])-1): # Right border
            neighbours = {
            (x-1,y):grid[x-1][y],
            (x+1,y):grid[x+1][y],
            (x-1,y-1):grid[x-1][y-1],
            (x,y-1):grid[x][y-1],
            (x+1,y-1):grid[x+1][y-1]
            }
        else: # Middle
            neighbours = {
            (x-1,y-1):grid[x-1][y-1],
            (x-1,y):grid[x-1][y],
            (x-1,y+1):grid[x-1][y+1],
            (x,y-1):grid[x][y-1],
            (x,y+1):grid[x][y+1],
            (x+1,y-1):grid[x+1][y-1],
            (x+1,y):grid[x+1][y],
            (x+1,y+1):grid[x+1][y+1]
            }
    neighbours.update({(x,y):2}) # Add the value of the cell for which we look the neighbours, make sure not to use the value 2 for either valueOn and valueOff as it's used here
    return neighbours
    
def countNeighbours(grid, x, y, valueOn, valueOff):
    """
        Function that, for a given grid and a given cell, identified with its coordinates x and y, return the number of cells in its neighbourhood that are on and the number that are off
        Parameters :
            - grid : a n x m array with the values of each cell, dead or alive
            - x : the coordinate of the cell on the x-axis
            - y : the coordinate of the cell on the y-axis
            - valueOn : the value that code the fact that a cell is on
            - valueOff : the value that code the fact that a cell is off
        Return :
            - numberOn, numberOff : the number of cells that are on and off in the neighbourhood
    """
    numberOn, numberOff = 0, 0
    neighbours = getNeighbours(grid, x, y)
    for key in neighbours.keys(): # we go through all the keys in the dict, so all the coordinates of the neighbours
        if(neighbours[key] == valueOn):
            numberOn += 1
        elif(neighbours[key] == valueOff):
            numberOff += 1
    return numberOn, numberOff
    
def applyRules(grid, valueOn, valueOff):
    """
        Function that, for a given grid, apply the rules of the game (see below for the detail)
        Parameters :
            - grid : a n x m array with the values of each cell, dead or alive
            - valueOn : the value that code the fact that a cell is on
            - valueOff : the value that code the fact that a cell is off
        Return :
            - nextGrid : the grid updated with the rules of the game (see below for the detail)
        Note : the rules are the following
            1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
            2. Any live cell with two or three live neighbours lives on to the next generation.
            3. Any live cell with more than three live neighbours dies, as if by overpopulation.
            4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
    nextGrid = [[valueOff for y in range(len(grid[0]))] for x in range(len(grid))]
    for x in range(len(grid)): # we go through all the point on the x-axis
        for y in range(len(grid[0])): # we go through all the point on the y-axis
            numberOn, numberOff = countNeighbours(grid, x, y, valueOn, valueOff)
            if(grid[x][y] == valueOn): # For the rules 1, 2 and 3
                if(numberOn < 2): # For the rule 1
                    nextGrid[x][y] = valueOff
                elif(numberOn == 2 or numberOn == 3): # For the rule 2
                    nextGrid[x][y] = valueOn
                elif(numberOn > 3): # For the rule 3
                    nextGrid[x][y] = valueOff
            elif(grid[x][y] == valueOff and numberOn == 3): # For the rule 4
                nextGrid[x][y] = valueOn
    return(nextGrid)
    
def showGrid(grid):
    """
        Useful fonction to show the grid, not absolutely necessary, can be not used
    """
    print(array(grid))
    
def generateRandomGrid(xSize, ySize, valueOn, valueOff):
    """
        Function that generate randomly a grid
        Parameters :
            - xSize : the size of the grid on the x-axis
            - ySize : the size of the grid on the x-axis
            - valueOn : the value that code the fact that a cell is on
            - valueOff : the value that code the fact that a cell is off
        Return :
            - grid : the grid generated randomly
    """
    grid = zeros((xSize, ySize), dtype=int)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] = choice([valueOn, valueOff]) # for each cell, we choose randomly a value between valueOn and valueOff
    return grid
          
# Values that code the fact that the cells are on and off (respectively alive and dead)
valueOn = 1
valueOff = 0

# There are two ways to create a grid :
# 1- Manually by creating a list of lists containing the same number of elements each time, where each element can be valueOn or valueOff (see above for the defined values
# example of a 3x3 manually definded grid : grid = [[valueOn,valueOn,valueOff],[valueOn,valueOff,valueOn],[valueOff,valueOn,valueOff]]
# 2- With the function generateRandomGrid(xSize, ySize, valueOn, valueOff) (see above for the definition of each parameter
# example of a 4x6 randomly generated grid : grid = generateRandomGrid(4, 6, valueOn, valueOff)

# Generation of the grid
grid = generateRandomGrid(10, 25, valueOn, valueOff)

# Number of turns
turns = 10
showGrid(grid) # Show the initial grid

for i in range(turns):
    print('----- Step',i+1,'-----')
    grid = applyRules(grid, valueOn, valueOff)
    
showGrid(grid)
