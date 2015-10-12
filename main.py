# Main program
import Classes
import tkinter as tk

def main():
    board = Classes.Board(6,6,6)
    board.printBoard()
    board.mainloop()

if __name__ == "__main__":
    main()
