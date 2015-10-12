import random
import tkinter as tk

# Sisältää pelilaudan ja sen manipulointiin tarvitavat metodit
class Board(list,tk.Frame):
    debug = True
    def __init__(self, height, width, mines,master=None):
        tk.Frame.__init__(self,master)
        self.height = height
        self.width = width
        self.mines = mines
        
        self.createBoard()
        self.addMines()
        self.updateTiles()
        self.grid()
        self.initUI()

    def initUI(self):
        # Configures the game grid and draws the buttons
        self.master.title("DOOMSWEEPER")
        
        # Configures the grid
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
       
            
    class Tile():    

        def __init__(self,y,x,master):
            self.master = master
            self.hidden = True
            self.y = y
            self.x = x
            self.hasMine = False
            self.adjacentMines = 0
            
        # TEMPORARY!
        
        
        def drawTile(self):
            self.canvas=tk.Canvas()
            self.canvas.grid(column=self.x,row=self.y)
            self.label = self.createLabel()
            self.label.grid()
            
            if self.hidden == True:
                # Lambda is the bee's knees!
                self.button = tk.Button(self.label, command=lambda: self.reveal())
                self.button.grid()

        def generateText(self):
            if self.hasMine == True:
                return "M"
            elif self.adjacentMines > 0:
                return str(self.adjacentMines)
            else:
                return ""

        def createLabel(self):
            # Creates and returns a label for a Tile
            if self.hasMine == True:
                icon = tk.PhotoImage(file="caco.gif")
                label = tk.Label(self.canvas,image=icon)
                self.icon = icon
                
                return label
            elif self.adjacentMines > 0:
                label= tk.Label(self.canvas, text=self.generateText())
                return label
            else:
                label = tk.Label(self.canvas, text="")
                return label
                
                
                
        def reveal(self):
            self.hidden = False
            self.button.destroy()
            if self.adjacentMines == 0 and self.hasMine == False:
                for i in range(self.y - 1,self.y + 2):
                    if i < 0 or i >= self.master.height:
                        continue
                    for j in range(self.x - 1, self.y + 2):
                        if j < 0 or j >= self.master.width:
                            continue
                        if self.master[i][j].hidden == True and self.master[i][j].hasMine == False:
                            if self.master[i][j].adjacentMines == 0:
                                self.master[i][j].reveal()
                            elif self.master[i][j].adjacentMines > 0:
                                self.master[i][j].hidden = False
                                self.master[i][j].button.destroy()
                            
                        


        
        

                  
                  
                
                
       
            
                
