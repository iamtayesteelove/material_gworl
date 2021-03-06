import tkinter as tk

# Inheritance
#     - We're going to be inherting the Tk class.
#     - This is so we can create a window.
#     - Inheritance is done by placing the class in the parenthesis
#       following the class name.
#

#class window(tk.Tk):
#    def __init__(self, pop_quiz):

class window(tk.Frame):
    COLOR_BG = '#b8e1ff'
    COLOR_WIN = '#e8aeb7'
    COLOR_BUTTON = '#a9fff7'
    COLOR_ACTIVE = '#94fbab'
    
    ROWS = 9
    COLS = 9
    CELL_SIZE = 50

    # @parameter 
    def __init__(self, root, game):
        self.root = root
        self.root.geometry("600x600")
        self.root.title("It's Sudoku Boo!")
        self.root.configure(bg='#aa1111')

        self.game = game
        self.selected_row = 0
        self.selected_col = 0

        tk.Frame.__init__(self, root)

        # set background color of canvas
        self.root.configure(bg=self.COLOR_BG)
        self.configure(bg=self.COLOR_BG)
        
        # Create the UI with the Board
        self.place(relx=.5, rely=.5, anchor=tk.CENTER)
        
        self.canvas = tk.Canvas(self, width=450, height=450)
        self.canvas.pack(fill=tk.BOTH)

        self.win_button = tk.Button(
            self, pady=20, 
            text='Wanna know if you won? Click me!', 
            command=self.__check_win,
            bg=self.COLOR_BUTTON, activebackground=self.COLOR_ACTIVE
        )
        self.win_button.pack(pady=20)

        self.__create_grid()
        self.__create_puzzle()

        # Bind Events
        # Left Mouse Press -> <Button-1>
        self.canvas.focus_set()
        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __create_grid(self):
        self.canvas.delete('grid')
        for i in range(10):
            w = 3 if i % 3 == 0 else 1
            
            # Horizontal Line
            x0, y0 = 0, i * self.CELL_SIZE
            x1, y1 = 450, y0
            
            self.canvas.create_line(x0, y0, x1, y1, fill='black', width=w, tag='grid')

            # Vertical Line
            x0, y0 = i * self.CELL_SIZE, 0
            x1, y1 = x0, 450

            self.canvas.create_line(x0, y0, x1, y1, fill='black', width=w, tag='grid')

    def __create_puzzle(self):
        self.canvas.delete('numbers')
        for row in range(9):
            for col in range(9):
                original = self.game.protected[row][col]
                num = self.game.board[row][col]
                
                if num != " ":
                    x, y = 25 + col * self.CELL_SIZE, 25 + row * self.CELL_SIZE
                    if original:
                        self.canvas.create_text(x, y, text=num, tag='numbers', fill='black', font=('Helvetica', '12', 'bold'))
                    else:
                        self.canvas.create_text(x, y, text=num, tag='numbers', fill='black', font=('Helvetica', '12'))

    # select a cell to enter the number
    # how do we show that? color the background?
    def __cell_clicked(self, event):
        self.canvas.delete('highlight')
        print(event.x, event.y)
        col, row = event.x//50, event.y//50
        
        print("\tcol: ", col, "\n", "\trow: ", row, sep='')

        # if out of bounds, return from function
        if col >= 9 or row >= 9:
            return

        self.selected_row, self.selected_col = row, col
        x, y = col * 50, row * 50
        print("\tx: ", x, "\n", "\ty: ", y, sep='')

        # draw the polygon
        self.canvas.create_polygon(x, y, x+50, y, x+50, y+50, x, y+50, 
                                   fill=self.COLOR_BG, tag='highlight')
        self.__create_grid()
        self.__create_puzzle()

    def __key_pressed(self, event):
        print(event.char)
        if not self.game.protected[self.selected_row][self.selected_col]:
            if event.char in "123456789":
                self.game.board[self.selected_row][self.selected_col] = event.char
                self.__create_puzzle()
            elif event.keysym == 'BackSpace' or event.keysym == 'Delete':
                self.game.board[self.selected_row][self.selected_col] = ' '
                self.__create_puzzle()

    def __check_win(self):
        correct = self.game.check4correct()
        print(correct)

        if correct:
            self.canvas.create_rectangle(75, 125, 375, 325, fill='pink', outline='')
            self.canvas.create_text(
                225, 225, 
                text='You are officially a\nMaterial Gworl!\n\nCongratulations!\nYou have won.',
                font=('Helvetica','15','bold'), justify=tk.CENTER
            ) 
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<Key>")
        else:
            pass