#!/usr/bin/python

# Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2


import random

class Queen:

    # Initializes a queen with default x,y values and y-key
    def __init__(self, x_position=0, y_position=0,y_key=0):
        self.y_key = y_key
        self.x_position = x_position
        self.y_position = y_position
        self.fitness = -1

    def set_position(self, x_position, y_position, y_key):
        self.y_key = y_key
        self.x_position = x_position
        self.y_position = y_position

    def set_fitness(self, fitness=0):
        self.fitness = fitness

    def print_queen(self):
        print("co-ords (%d,%d), key: %s, fitness %.2f" % (self.x_position,
                                                         self.y_position,
                                                         self.y_key,
                                                         self.fitness))
        
