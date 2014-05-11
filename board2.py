#!/usr/bin/python

# Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import random
import queen

class NQueensBoard:

    
    def __init__(self, queen_count=0):
        print "\nThis is the %d-Queen Problem!\n" % self.queen_count
        self.queen_count = queen_count
        self.random_set_up()

    def random_set_up(self):
        self.board = []
        for x in range(0, self.queen_count):
            x_list = []
            queen_y = get_queen_position()
            for y in range(0, self.queen_count):
                if (y == queen_y):
                    x_list.append(1)
                else:
                    x_list.append(0)
            self.board.append(x_list)

    def get_queen_position(self):
        random_key = random.SystemRandom()
        position = random_key.randint(0, self.queen_count * 10)
        return position % self.queen_count
