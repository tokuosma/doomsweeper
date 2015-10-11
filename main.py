# Main program
import Classes
import tkinter as tk

def main():
    board = Classes.Board(10,10,20)
    board.printBoard()
    board.mainloop()

if __name__ == "__main__":
    main()
