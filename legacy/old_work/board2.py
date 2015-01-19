#!/usr/bin/python

# Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import random
import queen

class NQueensBoard:

    
    def __init__(self, queen_count=0):
        self.queen_count = queen_count
        
        

    def key_set_up(self, board_key):
        pass
    
    def random_set_up(self):
        board = ""
        for i in range(0, self.queen_count):
            board += get_queen_position
        
        

    # Gives us a y-axis position for a queen
    def get_queen_position(self):
        random_key = random.SystemRandom()
        position = random_key.randint(0, self.queen_count * 10)
        return position % self.queen_count

    def key_set_up(self, board_key):
        pass

    

    
