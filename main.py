from board import Board

def main():
    rows = int(input("How many rows in the world"))
    columns = int(input("How many columns in the world"))

    world = Board(rows, columns)

    world.draw_board()

    user_action = ''
    while user_action !='q':
        user_action = 'PRESS Enter to add new generation or q to exit:'

        if user_action == '':
            world.update_board()
            world.draw_board()


main() 