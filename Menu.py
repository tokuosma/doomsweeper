import tkinter as tk
import Classes

class Application(tk.Tk):
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

        self.currentFrame = ""
        
        self.frames = {}
        for F in [MainMenu,NewGameMenu]:
            frame = F(self.container,self)
            self.frames[F] = frame
            
        self.showFrame(MainMenu)
        
    def showFrame(self, C):
        if self.currentFrame != "":
            self.currentFrame.grid_forget()
        self.currentFrame = self.frames[C]
        self.currentFrame.grid()
        

class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.config(width=controller.size[0], height=controller.size[1])

        bWidth = 20
        bHeight = 20

        label = tk.Label(self, text="DOOMSWEEPER",fg='red')
        buttonNewGame = tk.Button(self,width=bWidth, text="NEW GAME"
                                  ,command= lambda: self.controller.showFrame(NewGameMenu))
        buttonScores = tk.Button(self,width=bWidth, text="HIGH SCORES")
        buttonSettings = tk.Button(self,width=bWidth, text="SETTINS")
        buttonQuit = tk.Button(self,width=bWidth, text="QUIT", command=self.quit)
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

        label = tk.Label(self, text="NEW GAME")
        buttonBack = tk.Button(self, text="BACK",width=20,
                               command=lambda: self.controller.showFrame(MainMenu))
        label.grid()
        buttonBack.grid()
