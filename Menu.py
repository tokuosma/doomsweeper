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
        self.inputHeight = 16
        self.inputWidth = 16
        self.inputMines = 40
        self.createWidgets()
        
    def createWidgets(self):
        
        # Wraps the validateEntry method for use in entry validation
        validateEntry = self.register(self.validateEntry)
        
        # Labels
        labelTitle = tk.Label(self, text="NEW GAME",padx=10)
        labelHeight = tk.Label(self, text="Height:")
        labelWidth = tk.Label(self, text="Width:")
        labelMines = tk.Label(self, text="Mines")
        # Buttons
        buttonAddHeight = tk.Button(self,width=1,height=1,padx=0,pady=0, text="+",
                                    command=self.changeEntry("height",1))
        buttonSubHeight = tk.Button(self,width=1,height=1,padx=0,pady=0, text="-",
                                    command=self.changeEntry("height",-1))
        buttonAddWidth = tk.Button(self,width=1,height=1,padx=0,pady=0, text="+",
                                   command=self.changeEntry("width",1))
        buttonSubWidth = tk.Button(self,width=1,height=1,padx=0,pady=0, text="-",
                                   command=self.changeEntry("width",-1))
        buttonAddMines = tk.Button(self,width=1,height=1,padx=0,pady=0, text="+",
                                   command=self.changeEntry("mines",1))
        buttonSubMines = tk.Button(self,width=1,height=1,padx=0,pady=0, text="-",
                                   command=self.changeEntry("mines",-1))
        buttonBack = tk.Button(self, text="BACK",width=10,
                               command=lambda: self.controller.showFrame(MainMenu))
        buttonStart = tk.Button(self,width=10, text="START")
        # Entries
        entryHeight = tk.Entry(self,width=5,validate="all",vcmd=(validateEntry,'%S','%P'))
        entryHeight.insert(0,str(self.inputHeight))
        entryWidth= tk.Entry(self,width=5)
        entryWidth.insert(0, str(self.inputWidth))
        entryMines = tk.Entry(self,width=5)
        entryMines.insert(0,str(self.inputMines))

        # Grid all widgets
        labelTitle.grid(row=0, columnspan=3)
        labelHeight.grid(row=1,rowspan=2)
        labelWidth.grid(row=3,rowspan=2)
        labelMines.grid(row=5,rowspan=2)

        entryHeight.grid(row=1,rowspan=2, column=2)
        entryWidth.grid(row=3,rowspan=2, column=2)
        entryMines.grid(row=5,rowspan=2, column=2)

        buttonAddHeight.grid(row=1,column=1)
        buttonSubHeight.grid(row=2,column=1)
        buttonAddWidth.grid(row=3,column=1)
        buttonSubWidth.grid(row=4,column=1)
        buttonAddMines.grid(row=5,column=1)
        buttonSubMines.grid(row=6,column=1)
        buttonStart.grid(row=7,columnspan=3)
        buttonBack.grid(row=8,columnspan=3)
        
    def changeEntry(self,target,value):
        
        if target == "height":
            self.inputHeight += value
            print(self.inputHeight)
            
        elif target == "width":
            self.inputWidth += value
        elif target == "mines":
            self.inputMines += value

    def validateEntry(self,insert,text):
        # BROKEN!
        try:
            int(insert)
            if int(text) <= 100:
                return True
            else:
                self.insert(0,"100")
                return True
        except :
            return False
