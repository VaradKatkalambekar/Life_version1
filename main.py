from tablecheck import Tablecheck

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