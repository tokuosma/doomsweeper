# Main program
import Classes
import tkinter as tk

def main():
    mainWindow = tk.Frame(master=None)
    mainWindow.grid()
    mainWindow.master.title("Doomsweeper")
    
    board = Classes.Board(15,15,40,mainWindow)
    board.printBoard()
    board.mainloop()

if __name__ == "__main__":
    main()
