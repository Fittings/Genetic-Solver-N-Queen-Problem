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
        for x in range(0, self.queen_count):
            x_array = []
            queen_key = self.generate_position_key()   
            queen_y = self.get_position(queen_key) #y-coord of queen
            for y in range(0, self.queen_count):
                if (y == queen_y):
                    x_array.append(queen_key)
                else:
                    x_array.append("-1")
            self.board.append( x_array)
            
                                
    # Generates a random int and returns as a string to represent the queens
    # row position on the board.
    def generate_position_key(self):
        random_key = random.SystemRandom()
        position_key = random_key.randint(0, 10 ** self.queen_count) #XXX
        return str(position_key)
        

    # Returns the position of the queen in the given column
    # Doesn't work for anything greater than 9. ZZZ
    def get_position(self, position_key):
        temp_string = position_key
        queen_count_length = str(self.queen_count)
        while (len(temp_string) > len(queen_count_length)):
            temp_int = 0
            for i in range(0, len(temp_string)):
                temp_int += int(temp_string[i])
        
            temp_string = str(temp_int)
        return int(temp_string) % self.queen_count

    # Returns the number of collisions with other queens based on possible queen movement
    def get_queen_collisions(self, column):
        pass
        #ZZZ
                
        

    # Prints a visual-representation of the board and queens
    def print_board(self):
        for y in range(0, self.queen_count):
            row_string = ''
            for x in range(0, self.queen_count):
                if (int(self.board[x][y]) > 0):
                    row_string += 'Q '
                else:
                    row_string += '- '
            print row_string
                    



