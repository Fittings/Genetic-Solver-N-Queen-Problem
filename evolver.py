#!/usr/bin/python

#Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import board2

#This is used to control the board
class Evolver:

    # Initializes the lists of boards. Quantity of board and n value
    # for the n-Queen-Problem can be specified.
    # NOTE: Any value of queen_count above 10 will not work as intended
    def __init__(self, board_quantity=4, queen_count=8):
        queen_count = queen_count  
        print "This is the %d queen count problem" % queen_count
        self.board_list = []
        for i in range(0, board_quantity):
            self.board_list.append(board2.NQueensBoard(queen_count))
            
        self.fitness_sort()
        self.print_board_list()
        

    # Sorts the boards by their fitness value. [Lowest, ... , Highest]
    def fitness_sort(self):
        self.board_list = sorted(self.board_list,
                                key=lambda board: board.fitness)

    
    # Returns True if there is a solution. The solution will always be
    # at index 0 of board_list due to being sorted by fitness.
    def contains_solution(self):
        for i in range(0, len(self.board_list)):
            if (self.board_list[i].fitness == 0):
                return True
            else:
                return False
        
    # Prints the board list as a fitness value
    def print_board_list(self):
        for i in range(0, len(self.board_list)):
            print self.board_list[i].fitness


evolve = Evolver(20,4)





