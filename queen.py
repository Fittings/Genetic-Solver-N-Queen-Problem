#!/usr/bin/python

# Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2


import random

class Queen:

    # Initializes a queen with default x,y values and y-key
    def __init__(self, x_position=0, y_position=0,y_key=0):
        self.y_key = y_key
        self.x_postion = x_position
        self.y_position = y_key

    def set_position(self, x_position, y_position, y_key):
        self.y_key = y_key
        self.x_postion = x_postion
        self.y_position = y_key


    def print_queen(self):
        print("This queen has co-ords (%d,%d) and key: %s" % (self.x_postion,
                                                              self.y_position, self.y_key))
        
