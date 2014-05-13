#!/usr/bin/python

# Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import random



# Creates a board for the n-Queens Problem.
# This is only suitable for a queen count of max 10. (Change key implementation
# for a better fix)

class NQueensBoard:

    # Initializes the board, if no board key is given it will default to a
    # random board key.
    def __init__(self, queen_count, board_key=0):
        self.queen_count = queen_count
        self.board_key = board_key
        if (self.board_key == 0):
            self.board_key == random_set_up()
            
        
        

    def key_change(self, board_key):
        self.board_key = board_key
        self.fitness = self.board_key.get_fitness()
    
    def random_set_up(self):
        board = ""
        random_key = random.SystemRandom()
        board = random_key.randint(0, 10 ** (self.queen_count-1))
        return str(board)
        
        

    
    

    
