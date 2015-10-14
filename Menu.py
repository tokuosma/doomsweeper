import tkinter as tk
import Classes

class Application(tk.Tk):
    # Main application
    # (width,height)
    size = (198,198)
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False,height=False)
        
        self.container = tk.Frame(self, width=self.size[0], height=self.size[1])        
        self.container.master.title("DOOMSWEEP")
        self.container.grid()
        self.container.rowconfigure(0)
        self.container.columnconfigure(0)
        # Contains the frame currently in container
        self.currentFrame = ""

        # Dictionary containing the main menu and all frames accessible from main menu
        self.frames = {}
        for F in [MainMenu,NewGameMenu]:
            frame = F(self.container,self)
            self.frames[F] = frame
        
        self.showFrame(MainMenu)
        
    def showFrame(self, C):
        # Removes current frame and draws frame C
        # Checks if a frame is loaded
        if self.currentFrame != "":
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

class NewGameMenu(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.config(width=controller.size[0], height=controller.size[1])
        
        labelTitle = tk.Label(self, text="NEW GAME",padx=10)
        labelHeight = tk.Label(self, text="Height:")
        labelWidth = tk.Label(self, text="Width:")
        labelMines = tk.Label(self, text="Mines")

        buttonAddHeight = tk.Button(self, text="+")
        buttonSubHeight = tk.Button(self, text="-")
        buttonAddWidth = tk.Button(self, text="+")
        buttonSubWidth = tk.Button(self, text="-")
        buttonAddMines = tk.Button(self, text="+")
        buttonSubMines = tk.Button(self, text="-")
        buttonBack = tk.Button(self, text="BACK",width=20,
                               command=lambda: self.controller.showFrame(MainMenu))
                
        entryHeight = tk.Entry(self)
        entryWidth= tk.Entry(self)
        entryMines = tk.Entry(self)
        
        labelTitle.grid(row=0, columnspan=3)
        labelHeight.grid(row=1,rowspan=2)
        labelWidth.grid(row=3,rowspan=2,sticky=tk.W)
        labelMines.grid(row=5,rowspan=2,sticky=tk.W)

        entryHeight.grid(row=1,rowspan=2, column=2)
        entryWidth.grid(row=3,rowspan=2, column=2)
        entryMines.grid(row=5,rowspan=2, column=2)

        buttonAddHeight.grid(row=1,column=1)
        buttonSubHeight.grid(row=2,column=1)
        buttonBack.grid()
        
