from sudoku import sudoku
from layout import window
from tkinter import Tk

game = sudoku()
game.test_set_correct_and_check()
game.print_board()

root = Tk()
window(root, game)
root.mainloop()