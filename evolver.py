#!/usr/bin/python

#Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import random
import board2


#This is used to control the board
class Evolver:

    # Initializes the lists of boards. Quantity of board and n value
    # for the n-Queen-Problem can be specified.
    # NOTE: Any value of queen_count above 10 will not work as intended
    def __init__(self, board_quantity=4, queen_count=8):
        self.queen_count = queen_count  
        print "This is the %d-Queen-Problem\t" % self.queen_count
        self.board_list = []
        for i in range(0, board_quantity):
            self.board_list.append(board2.NQueensBoard(self.queen_count))
            
        self.fitness_sort()
        self.print_board_list()
        

    # Sorts the boards by their fitness value. [Lowest, ... , Highest]
    def fitness_sort(self):
        self.board_list = sorted(self.board_list,
                                key=lambda board: board.fitness)

    # This will continue to evolve the board until a solution is found.
    def evolve_board(self):
        epochs = 0
        random_key = random.SystemRandom()
        while not(self.contains_solution()):
            while (random_key.randint(0, 1000) < 10):
                self.mutate()

            epochs += 1
        self.board_list[0].print_board()
        print "Done in %d epochs" % epochs

    #Randomly moves queen on a random board
    def mutate(self):
        random_key = random.SystemRandom()
        random_board_no = random_key.randint(0, self.queen_count-1)
        board_key = list(self.board_list[random_board_no].board_key)
        random_index = random_key.randint(0, len(board_key)-1)
        board_key[random_index] = str(random_key.randint(0, self.queen_count-1))
        self.board_list[random_board_no].key_change(''.join(board_key))
        
        
        
    # Returns True if there is a solution. The solution will always be
    # at index 0 of board_list due to being sorted by fitness.
    def contains_solution(self):
        if (self.board_list[0].fitness == 0):
            return True
        else:
            return False
        
    # Prints the board list as a fitness value
    def print_board_list(self):
        for i in range(0, len(self.board_list)):
            print self.board_list[i].fitness


evolve = Evolver(60,4)
#evolve.contains_solution()
evolve.evolve_board()




