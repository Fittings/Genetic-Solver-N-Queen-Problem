#!/usr/bin/python

# Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import random

class NQueens:
    'This class is used to create a nxn chessboard and ' \
        '"evolve" a non-conflicting solution of Queen Placements'

        
    # Initializes a board with n Queens in random positions
    def __init__(self, queen_count=0):
        self.queen_count = queen_count
        self.random_set_up()

    # Sets the board with queens placed on every column with random
    # row positions
    def random_set_up(self):
        print "This is the %d-Queen problem!" % self.queen_count
        self.board = []
        for i in range(0, self.queen_count):
            self.board.insert(i, self.generate_position_key())
                                
    # Generates a random int and returns as a string to represent the queens
    # row position on the board.
    def generate_position_key(self):
        random_key = random.SystemRandom()
        position_key = random_key.randint(0, 10 ** self.queen_count) % self.queen_count
        return str(position_key)
        

    # Returns the position of the queen in the given column
    def get_position(self, position_key):
        temp_string = position_key
        while (len(temp_string) != 1):
            temp_int = 0
            for i in range(0, len(temp_string)):
                temp_int += int(temp_string[i])
        
            temp_string = str(temp_int)
        return int(temp_string)

    # Prints a visual-representation of the board and queens
    # Currently side-ways :) ZZZ
    def print_board(self):
        for i in range(0, self.queen_count):
            queen_pos = self.get_position(self.board[i])
            row_string = ''
            for i in range(0, self.queen_count):
                if (i == queen_pos):
                    row_string += 'X '
                else:
                    row_string += '- '
            print row_string

    
    
