import random
import tkinter as tk

# Sisältää pelilaudan ja sen manipulointiin tarvitavat metodit
class Board(list,tk.Frame):
    debug = True
    # format: (y,x)
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    def __init__(self, height, width, mines,master):
        tk.Frame.__init__(self,master)
        #Init. attributes
        self.height = height
        self.width = width
        self.mines = mines
        self.master = master
        # Creates and initializes the board
        self.createBoard()
        self.addMines()
        self.updateTiles()
        # Init. the UI
        self.grid()
        self.initUI()

    def initUI(self):
        # Configures the game grid and draws the buttons
      
        # Configures the grid layout
        for i in range(self.width):
            self.columnconfigure(i, pad=1)
        for i in range(self.height):
            self.rowconfigure(i, pad=1)
        # Draws tiles
        for i in range(self.height):
            for j in range(self.width):
                self[i][j].drawTile()
            
    def createBoard(self):
        # Fills board of specified dimensions with Tiles
        for y in range(self.height):
            self.append([])
            for x in range(self.width):
                self[y].append(self.Tile(y,x,self))

    def printBoard(self):
        # Prints Board to console
        for y in range(self.height):
            print("") #newline
            for x in range(self.width):
                if(self[y][x].hidden and self.debug == False):
                    print(" H ",end="")
                else:
                    if( self[y][x].hasMine == True):
                        print(" M ",end="")
                    else:
                        print(" %s " % str(self[y][x].adjacentMines),end="" )
        print("BUTT")
                        
    def addMines(self):
        # Adds the number of mines specified to board
        count=self.mines
        while(count > 0):
            x = random.randint(0,self.width-1)
            y = random.randint(0,self.height-1)
            print("Arvottiin: %i ja %i"%(x,y))
            if(self[y][x].hasMine == False):
                self[y][x].hasMine = True
                count -= 1
                
    def updateTiles(self):
        # For each Tile on Board, counts the mines on surrounding tiles
        # and updates the value of adjacentMines on Tile.
        for y in range(self.height):
            for x in range(self.width):
                count = 0
                for i in range(y-1,y+2):
                    # Skips rows not on Board
                    if i < 0 or i >= self.height:
                        continue
                    for j in range(x-1,x+2):
                        # Skips columns not on Board
                        if j < 0 or j >= self.width:
                            continue
                        # Skips curent tile
                        elif i == y and j == x:
                            continue
                        elif self[i][j].hasMine == True:
                            count += 1                                            
                self[y][x].adjacentMines = count

    def gameOver(self):
        print("GAMEOVER")      
            
    class Tile():    

        def __init__(self,y,x,master):
            self.master = master
            self.hidden = True
            self.y = y
            self.x = x
            self.hasMine = False
            self.adjacentMines = 0
        
        def drawTile(self):
            # Draws the Tile to the Board at the beginnig of the game
            # First creates a canvas and assigns it to the proper place on grid
            self.canvas=tk.Canvas()
            self.canvas.grid(column=self.x,row=self.y)
            # Next creates a label for tile and places it on canvas
            self.label = self.createLabel(self.canvas)
            self.label.grid()
            # Finally creates a button on top of the label
            self.button = tk.Button(self.label,bd=3, command=lambda: self.reveal())
            self.button.grid()

        def generateText(self):
            # Generates a string containing the number of mines for the tile label
            if self.adjacentMines > 0:
                return str(self.adjacentMines)
            else:
                return ""

        def createLabel(self,master):
            # Creates and returns a label for a Tile.
            # if Tile has mine, returns a label with image
            if self.hasMine == True:
                icon = tk.PhotoImage(file="caco.gif")
                label = tk.Label(master,image=icon)
                # saves the photo as an attribute
                self.icon = icon               
                return label
            # if no tile has no mine, returns a label containing the number of mines
            # on adjacen squares
            elif self.adjacentMines > 0:
                label= tk.Label(self.canvas, text=self.generateText())
                return label
            # If no mines on adjacent squares, returns an empty label
            else:
                label = tk.Label(self.canvas, text="")
                return label
                               
        def reveal(self):
            # Command issued when button over tile is pressed.
            # Destroys the button and makes the label visible
            # Also reveals neighbouring tiles that do not contain mines
            # and all empty tiles connected to a revealed empty tile            
            self.hidden = False
            self.button.destroy()

            if self.hasMine == True:
                self.master.gameOver()
            elif self.adjacentMines == 0:
                for direction in self.master.directions:
                    y = self.y + direction[0]
                    x = self.x + direction[1]
                    if self.isOnBoard(y,x):
                        if self.master[y][x].hidden == True:
                            self.master[y][x].reveal()

        def isOnBoard(self,y,x):
            # if a tile at coordinates (x,y) is on board returns True
            if y >= 0 and y < self.master.height:
                if x >= 0 and x < self.master.width:
                    return True
                else:
                    return False
            else:
                return False
                
                
                        


        
        

                  
                  
                
                
       
            
                
