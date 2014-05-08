#!/usr/bin/python

# Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2


import random

class Queen:

    # Initializes a queen with default x,y values and y-key
    def __init__(self, x_position=0):
        self.y_key = self.generate_position_key()
        self.x_postion = x_postion
        self.y_position = self.get_position(self.y_key)

    # Generates a random int and returns as a string to represent the queens
    # row position on the board.
    def generate_position_key(self):
        random_key = random.SystemRandom()
        position_key = random_key.randint(0, 10 ** self.queen_count)
        return str(position_key)

    def get_position(self, position_key, board_size):
        temp_string = position_key
        queen_count_length = str(board_size)
        while (len(temp_string) > len(queen_count_length)):
            temp_int = 0
            for i in range(0, len(temp_string)):
                temp_int += int(temp_string[i])
        
            temp_string = str(temp_int)
            
        return int(temp_string) % board_size

nqueen = Queen()
