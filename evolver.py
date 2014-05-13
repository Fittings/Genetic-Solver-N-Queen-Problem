#!/usr/bin/python

#Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import board2

#This is used to control the board
class Evolver:

    def __init__(self, board_quantity=10, queen_count=8):
        queen_count = queen_count  #Queen count can't be higher than 10
        print "This is the %d queen count problem" % queen_count
        self.board_list = []
        for i in range(0, board_quantity):
            self.board_list.append(board2.NQueensBoard(queen_count))
        self.fitness_sort()

    def fitness_sort(self):
        pass


evolve = Evolver(50)





