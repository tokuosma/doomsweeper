import tkinter as tk
import Classes

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)
        self.container.master.title("DOOMSWEEP")
        self.container.grid()
        self.container.rowconfigure(0)
        self.container.columnconfigure(0)

        self.frames = {}
        for F in [MainMenu]:
            frame = F(self.container,self)
            self.frames[F] = frame
            frame.grid()
        

class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        label = tk.Label(self, text="DOOMSWEEPER",fg='red')
        buttonNewGame = tk.Button(self, text="NEW GAME")
        label.grid()
        buttonNewGame.grid()
