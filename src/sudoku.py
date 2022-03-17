import random
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
    # __init__(self)
    #     parameter(s)
    #         - self
    #     return value(s)
    #         - none
    def __init__(self):
        file = open("src/sudoku_sheets/starting_data_set.csv", "r")
        data = file.read().split("\n")
        self.board_string = ''.join(data)
        file.close()
        
        selection = random.choice(data)
        self.pop_quiz = selection[0:81]
        self.solution = selection[82:]
        self.protected = [[None for i in range(self.SIZE)] for j in range(self.SIZE)]

        # Populate board with quiz
        #     if the character is '0', leave it blank
        i = 0
        
        for row in range(9):
            for col in range(9):
                self.protected[row][col] = True if self.pop_quiz[i] != '0' else False
                
                if self.pop_quiz[i] != "0":
                    self.board[row][col] = self.pop_quiz[i]
                i += 1


    def print_board(self):
        for row in range(9):
            print(self.board[row])

        for row in range(9):
            print(self.protected[row])


    def check4correct(self):
        correct = True
        number_list = [str(i) for i in range(1, 10)]

        
        # Check Rows
        for row in self.board:
            if set(row) != set(number_list):
                correct = False


        # Construct Columns
        if correct:
            columns = []
            for col in range(9):
                column = []
                for row in range(9):
                    column.append(self.board[row][col])
    
                columns.append(column)
                
            # Check Columns
            for col in columns:
                if set(col) != set(number_list):
                    correct = False


        # Construct Grids
        if correct:
            grids = []
            row_offset = 0
            col_offset = 0
            
            for cell in range(9):
                if cell ==  3 or cell == 6:
                    row_offset += 3 
                    col_offset = 0
                
                grid = []
                for row in range(3):
                    grid_row = []
                    for col in range(3):
                        grid_row.append(self.board[row + row_offset][col + col_offset])
                    
                    grid += grid_row
    
                col_offset += 3
                grids.append(grid)
    
    		# Check Grids
            for grid in grids:
                if set(grid) != set(number_list):
                    correct = False
        
                
        return correct

        
    def test_set_correct_and_check(self):
        i = 0
        
        for row in range(9):
            for col in range(9):
                if self.solution[i] != "0":
                    self.board[row][col] = self.solution[i]
                i += 1

        self.check4correct()