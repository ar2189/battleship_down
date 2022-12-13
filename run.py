from random import randint

# Board for holding the ship locations
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]

# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]


def print_board(board):
    """
    Function to display board with rows and columns.
    By giving the columns number, it differentiates againts the row.
    """
    print(" A B C D E F G H")
    print(" +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


letters_to_numbers  = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7
}

def create_ships(board):
    """
    Function to create ships inside the board randomely.
    With this you can decide how many ships to create.
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column = 'X']