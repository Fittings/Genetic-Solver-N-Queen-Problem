#!/usr/bin/python

# Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import random
import queen

class NQueensBoard:
    'This class is used to create a nxn chessboard and ' \
        '"evolve" a non-conflicting solution of Queen Placements'

        
    # Initializes a board with n Queens in random positions
    def __init__(self, queen_count=0):
        self.queen_count = queen_count
        self.random_set_up()

    # Sets the board with queens placed on every column with random
    # row positions
    def random_set_up(self):
        print "This is the %d-Queen problem!\n" % self.queen_count
        self.board = []
        self.queen_priority = []
        for x in range(0, self.queen_count):
            x_list = [] #The '2d' part of the list
            queen_key = self.generate_position_key()   
            queen_y = self.get_position(queen_key) #y-coord of the queen
            for y in range(0, self.queen_count):
                if (y == queen_y):
                    x_list.append(queen.Queen(x, queen_y, queen_key))
                    
                else:
                    x_list.append("0")
            self.board.append( x_list)
            self.queen_priority.append(self.board[x][y])
            
    #ZZZ                            
    # Generates a random int and returns as a string to represent the queens
    # row position on the board.
    def generate_position_key(self):
        random_key = random.SystemRandom()
        position_key = random_key.randint(0, 10 ** self.queen_count)
        return str(position_key)
        
    #ZZZ 
    # Returns the position of the queen in the given column.
    def get_position(self, position_key):
        temp_string = position_key
        queen_count_length = str(self.queen_count)
        while (len(temp_string) > len(queen_count_length)):
            temp_int = 0
            for i in range(0, len(temp_string)):
                temp_int += int(temp_string[i])
        
            temp_string = str(temp_int)
        return int(temp_string) % self.queen_count



    #ZZZ    
    # Makes a list of the queens in order of fitness. Queens are identified by their
    # x co-ordinate.
    def set_queen_priorities():
        for i in range(0, self.queen_count):
            pass
            
    #ZZZ    
    # Returns the number of collisions with other queens based on possible queen movement
    def get_queen_collisions(self, column):
        pass
        
                
        

    #def print_queen_order(self):
    #    for i in range(0, self.queen_count):
    #        print ""

    
    # Prints a visual-representation of the board and queens
    def print_board(self):
        for y in range(0, self.queen_count):
            row_string = ''
            for x in range(0, self.queen_count):
                if (self.board[x][y] == "0"):
                    row_string += '- '
                else:
                    row_string += 'Q '
            print row_string
                    



