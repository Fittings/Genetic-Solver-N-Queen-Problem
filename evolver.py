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
        self.board_quantity = board_quantity
        print "This is the %d-Queen-Problem\t" % self.queen_count
        self.board_list = []
        for i in range(0, board_quantity):
            self.board_list.append(board2.NQueensBoard(self.queen_count))
            
        self.fitness_sort()
        
        

    # Sorts the boards by their fitness value. [Lowest, ... , Highest]
    def fitness_sort(self):
        self.board_list = sorted(self.board_list,
                                key=lambda board: board.fitness)

    # This will continue to evolve the board until a solution is found.
    # epochs counter is representative of how many generations it takes.
    def evolve_board(self):
        epochs = 0
        random_key = random.SystemRandom()
        while not(self.contains_solution()):
            #ZZZ
            #Mutate a board with 1/100 chance
            #while (random_key.randint(0, 1000) < 10):
               # self.mutate()

            #Choose the best boards and combine them to create new boards
            self.repopulate()
                
            epochs += 1
        self.board_list[0].print_board()
        print "Done in %d epochs" % epochs

    #Randomly moves queen on a random board
    def mutate(self, board):
        """board_key = list(self.board
        
        # Chance of mutation at each point
        random_key = random.SystemRandom()
        for i in range
        if (random_key.randint(0, 1000) > 10):
        
        
        random_board_no = random_key.randint(0, self.queen_count-1)
        board_key = list(self.board_list[random_board_no].board_key)
        random_index = random_key.randint(0, len(board_key)-1)
        board_key[random_index] = str(random_key.randint(0, self.queen_count-1))
        self.board_list[random_board_no].key_change(''.join(board_key))"""
        pass

    # Repopulates the boards.
    # How often a single board can 'breed' is random-influenced by fitness
    def repopulate(self):
        # Create an intermediate population based on roulette
        new_board_list = []
        for i in range(0, self.board_quantity - 1):
            new_board_list.append(self.roulette_wheel())
            
        # Perform crossovers with 2 parents with a particular crossover rate
        random_key = random.SystemRandom()
        crossover_rate = 95    
        i = 0
        # Crossovers parent i and then the next parent in the list.
        while (i < len(self.board_list)):
            if (random_key.randint < crossover_rate):
                j = (i+1) % len(new_board_list) #Uses mod for non-even len lists
                new_board_list[i].append(board2.NQueensBoard(self.queen_count
                                                             , crossover(i, j))
                new_board_list[i+1].append(board2.NQueensBoard(self.queen_count
                                                               ,crossover(j, i))
            i += 2
                

    # This exists so I can easily change what type of crossover is used.
    def crossover(self, board1, board2):
        return single_crossover(board1, board2)


    # Single point crossover
    def single_crossover(self, board1, board2):
        crossover_point = random.SystemRandom().randint(0, len(board1)-1)
        new_board = board1[:crossover_point]
        new_board += board2[crossover_point:]
        print new_board
        return new_board
            
        

    # Returns an index for the board choosen by the roulette wheel
    # This favours the boards with higher fitness
    def roulette_wheel(self):
        #Sum
        fitness_sum = 0.0
        for i in range(0, self.board_quantity-1):
            fitness_sum += self.board_list[i].fitness
        #Select
        random_key = random.SystemRandom()
        random_select = random_key.randint(0, int(round(fitness_sum)))
        #Loop
        fitness_sum = 0.0
        i = 0
        while not(fitness_sum > random_select):
            fitness_sum += self.board_list[i].fitness
            i += 1
        return i
        

 
        
        
        
        
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


evolve = Evolver(11,4)
#evolve.contains_solution()
evolve.evolve_board()




