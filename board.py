# For creating the board.. we need a few functions
# how will the board be created? The rows and columns?
# how will you check all the cells on the board and make changes?
# how will you check the neighbours and decide if a cell lives or dies??
# how will you reprint?


from cell import Cell
from random import randint

class Board:
    def __init__(self, rows, columns ):
        self._rows = rows
        self._columns = columns
        self._grid = [[Cell for col_cells in range(self._columns)] for row_cells in range(self._rows)]

        self._generate_board()

    def draw_board(self):
        print('This is a board')
        for row in self._grid:
            for column in row:
                print (column.get_print_character(),end='')
            print () # to create a new line pr. row.

    def _generate_board(self):
        for row in self._grid:
            for column in row:
                #we set a small chance to make sure our world is not really cluttered.
                chance_number = randint(0,5)
                if chance_number == 1:
                    column.set_alive()
