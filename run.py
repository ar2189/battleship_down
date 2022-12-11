# Battleship

# Imports
import copy as c
import os
import random as rand


class Game(object):
    """
    Main board class. Sets board size, the number of players
    and the ships placed randomely.
    """
    def __init__(self, players):
        self.guesses = 5
        self.player_list = []
        for player in range(players):
            self.player_list.append(self.guesses)
        self.current_player = 1
        self.board = self.creatematrix(5, 5)
        self.board_visible = c.deepcopy(self.board)
        self.ship_row = rand.randint(0, 4)
        self.ship_col = rand.randint(0, 4)
        self.guess_row = 0
        self.guess_col = 0


    def print_board(self, board_in):
        """
        Defining the print board.
        x represents rows.
        y represents columns.
        """
        x = 0
        y = 0
        for column in board_in:
            y = 0
            for row in column:
                if y == 0:
                    print(" ", row, end=" ")
                elif y == len(board_in[x]):
                    print("", row, end=""):
                else:
                    print(row, end=" ")
                y += 1
            print()
            x += 1
        return None    
