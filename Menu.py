import tkinter as tk
import Classes

class Application(tk.Tk):
    # Main application
    # (width,height)
    size = (198,198)
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Locks the window size
        self.resizable(width=False,height=False)

        # Top level frame
        self.container = tk.Frame(self, width=self.size[0], height=self.size[1])        
        self.container.master.title("DOOMSWEEP")
        self.container.grid()
        
        # Contains the frame currently in container
        self.currentFrame = ""

        # Dictionary containing the main menu and all frames accessible from main menu
        self.frames = {}
        for F in [MainMenu,NewGameMenu]:
            # Initializes all frames (master = container, controller = self)
            frame = F(self.container,self)
            self.frames[F] = frame
        
        self.showFrame(MainMenu)

    #Removes current frame and draws frame C        
    def showFrame(self, C):
        # Checks if a frame is loaded
        if self.currentFrame != "":
            # If a frame is loaded, removes it from grid
            self.currentFrame.grid_remove()
        self.currentFrame = self.frames[C]
        self.currentFrame.grid()
        

class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.config(width=controller.size[0], height=controller.size[1])
        # Button height and width for main menu
        bWidth = 20
        bHeight = 20
        
        # Create widgets
        label = tk.Label(self, text="DOOMSWEEPER",fg='red')
        buttonNewGame = tk.Button(self,width=bWidth, text="NEW GAME"
                                  ,command= lambda: self.controller.showFrame(NewGameMenu))
        buttonScores = tk.Button(self,width=bWidth, text="HIGH SCORES")
        buttonSettings = tk.Button(self,width=bWidth, text="SETTINGS")
        buttonQuit = tk.Button(self,width=bWidth, text="QUIT", command=self.quit)
        # Grid widgets
        label.grid()
        buttonNewGame.grid()
        buttonScores.grid()
        buttonSettings.grid()
        buttonQuit.grid()

# Menu that enables the starting of a new game and setting up options for the game        
class NewGameMenu(tk.Frame):
    
    fields = ["Height", "Width", "Mines"]

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.config(width=controller.size[0], height=controller.size[1])
        self.createWidgets()
        
    def createWidgets(self):
        title = tk.Label(self, text="NEW GAME")
        title.grid()
        for field in self.fields:
            row = tk.Frame(self)
            label = tk.Label(row, text=field, width=6)
            addBtn = tk.Button(row, text="+", padx=1, pady=1, width=1, height=1, anchor=tk.CENTER)
            subBtn = tk.Button(row, text="-", padx=1, pady=1, width=1, height=1)
            entry = tk.Entry(row, width=10)
            row.grid()
            label.grid(row=1, padx=3, rowspan=2, column=1, sticky='e')
            addBtn.grid(row=1, padx=10, column=2, sticky='w')
            subBtn.grid(row=2, padx=10,  column=2, sticky='w')
            entry.grid(row=1, padx=3, rowspan=2, column=3, sticky='e')
            
        backButton = tk.Button(self, text="Back", command=lambda:self.controller.showFrame(MainMenu))
        backButton.grid()
        
        
    # Command for + and - buttons to change the value in the entry field
    def changeEntry(self,target,value):
        # TBD
        pass
    
    # Function for new game menu entry validation. insert is the text to be inserted
    # to the entry and text is the string in the entry field after insertion
    def validateEntry(self,insert,text,name):
        # TBD
        pass
        
            
