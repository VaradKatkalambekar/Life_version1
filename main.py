from tablecheck import Tablecheck
from cell import Cell

mat = Tablecheck()
mat.print_board()

def check_conditions(self,triggered_row,triggered_column):
    # now here we check the conditions of the game, we are going to need three rows, the current one, the old one, or the next one.. so the rane of the iteration is [-1,1] but in python we show it as (-1,2)
    min_para = -1
    max_para = 2

    #we have to know the number of the neighbours right? so now we add all the available neighbors to an array and check the number in the end to excute necessary statements
    neighbours = []
    for row in range(min_para, max_para):
        for column in range(min_para, max_para):
            
            neigh_row = triggered_row + row
            neigh_column = triggered_column + column

            neigh_exists = True

            if (neigh_row) == triggered_row and (neigh_column) == triggered_column:
                #the same cell cannot be the neighbour
                neigh_exists = False

            if (neigh_row) < 0  or neigh_row >= self._rows:
                neigh_exists = False

            if (neigh_column) < 0 or neigh_column >= self._columns:
                neigh_exists = False

            if neigh_exists:
                neighbours.append(self._grid[neigh_row][neigh_column])
    return neighbours



def update_board(self):
    print('Board is being updates')

    borns =[]
    dies = []
    lives = []

    for row in range(len(self._grid)):
        for column in range(len(self._grid[row])):

           check_conditions =  self.check_conditions(row,column)

           neigh_alive = []

           for i in check_conditions:
               if i.is_alive():
                   neigh_alive.append(i)
            
            cell_obj = self._grid[row][column]
            status_main_cell = cell_obj.is_alive()


            #if the cell is alive, we now see the number of neighbours...
            if status_main_cell:
                if len(neigh_alive) < 2 or len(neigh_alive) > 3:
                    dies.append(cell_obj)
                
                if len(neigh_alive) == 2 or len(neigh_alive) == 3:
                    lives.append(cell_obj)

            else:
                if len(neigh_alive) == 3:
                    lives.append(cell_obj)

    for cell_items in lives:
        cell_items.set_alive()

    for cell_items in dies:
        cell_items.set_dead()

