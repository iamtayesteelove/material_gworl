# What is a class? Template or blueprint for an object.

# What is an object? Instance of a class, created based on it's structure.

class sudoku:
    # Member Variables
    #     - Variables that a class has access to.
    #     - Sometimes referred to as properties.

    # size of the board
    SIZE = 9

    # logical sudoku board
    board = [[" " for i in range(9)] for i in range(9)]

    # Constructor --> The function that is called when you make an object.
    #     - Perform any setup as necessary in this function.
    # def __init__(this):
    def __init__(this):
        pass