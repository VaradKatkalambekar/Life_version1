#first we should see what are the phases a cell goes through - 
# 1 - Dead
# 2 - Set it as Alive
# 3 - Check if its Alive
# 4 - What should be shown on the output

# defining a class for the cell



class Cell:
    def __init__(self):
        '''initial status of the cell'''
        self._status = 'Dead'
    
    def set_dead(self):
        '''We can set if the cell is dead or alive'''
        self._status = 'Dead'

    def set_alive(self):
        '''We can set if the cell is dead or alive'''
        self._status = 'Alive'

    def is_alive(self):
        '''We check if a cell is dead or alive'''
        if self._status == 'Alive':
            return True 
        else:
            return False


    def what_to_print(self):
        '''We decide what to print in the cell value'''
        if self.is_alive():
            return 0
        else:
            return 'X'


