import random

class Board(list):
    # The game board, basically just a two dimensional array containing Tiles
    def __init__(self, height, width, mines):
        self.height = height
        self.width = width
        self.mines = mines
        self.createBoard()
        self.addMines()
        self.updateTiles()
        
    def createBoard(self):
        # Fills board of specified dimensions with Tiles
        for y in range(self.height):
            self.append([])
            for x in range(self.width):
                self[y].append(Tile(y,x))

    def printBoard(self):
        # Prints Board to console
        for y in range(self.height):
            print("") #newline
            for x in range(self.width):
                if(self[y][x].checkHidden()):
                    print(" H ",end="")
                else:
                    if( self[y][x].checkHasMine() == True):
                        print(" M ",end="")
                    else:
                        print(" %s " % str(self[y][x].checkAdjacentMines()),end="" )
                        
    def printBoardDebug(self):
        # Prints Board to console (no hidden tiles)
        for y in range(self.height):
            print("") #newline
            for x in range(self.width):
                if(self[y][x].checkHasMine == True):
                    print(" M ", end="")
                else:
                    if( self[y][x].checkHasMine() == True):
                        print(" M ",end="")
                    else:
                        print(" %s " % str(self[y][x].checkAdjacentMines()),end="" )

    def addMines(self):
        # Adds the number of mines specified to board
        count=self.mines
        while(count > 0):
            x = random.randint(0,self.width-1)
            y = random.randint(0,self.height-1)
            print("Arvottiin: %i ja %i"%(x,y))
            if(self[y][x].hasMine == False):
                self[y][x].addMine()
                count -= 1
                
    def updateTiles(self):
        # For each Tile on Board, counts the mines on surrounding tiles
        # and updates the value of adjacentMines on Tile.
        for y in range(self.height):
            for x in range(self.width):
                print("Starting work on tile (y=%i,x=%i)"%(y,x))
                count = 0
                for i in range(y-1,y+2):
                    # Skips rows not on Board
                    if i < 0 or i >= self.height:
                        print("Skipping row %i."%i)
                        continue
                    for j in range(x-1,x+2):
                        # Skips columns not on Board
                        if j < 0 or j >= self.width:
                            print("Skipping column %i"%j)
                            continue
                        # Skips curent tile
                        elif i == y and j == x:
                            print("Skipping current tile")
                            continue
                        elif self[i][j].checkHasMine() == True:
                            count += 1                                            
                self[y][x].adjustAdjacentMines(count)
                
class Tile(object):    
    # Cell unit of Board
    def __init__(self,y,x):
        self.hidden = True
        self.y = y
        self.x = x
        self.hasMine = False
        self.adjacentMines = 0
    # Accessor functions
    def checkHidden(self):
        return self.hidden
    def reveal(self):
        self.hidden = False
    def checkHasMine(self):
        return self.hasMine
    def addMine(self):
        self.hasMine = True
    def checkAdjacentMines(self):
        return self.adjacentMines
    def adjustAdjacentMines(self, value):
        self.adjacentMines = value
    
board = Board(20,20,10)
#board.printBoard()
board.printBoardDebug()


