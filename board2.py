#!/usr/bin/python

# Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import random



# Creates a board for the n-Queens Problem.
# This is only suitable for a queen count of max 10. (Change key implementation
# for a better fix)

class NQueensBoard:

    # Initializes the board, if no board key is given it will default to a
    # random board key based on the queen_count.
    # Initializes the fitness variable by default.
    def __init__(self, queen_count, board_key=0):
        self.queen_count = queen_count
        self.board_key = str(board_key)
        if (self.board_key == "0"):
            self.board_key = self.random_set_up()
        self.fitness = self.find_fitness()
                
    def get_fitness(self):
        return self.fitness
        
    def key_change(self, board_key):
        self.board_key = str(board_key)
        self.fitness = self.find_fitness()

    # Creates a randomly generated (string) board key and returns it.
    def random_set_up(self):
        board = ""
        random_key = random.SystemRandom()
        for i in range(0, self.queen_count):
            board += str(random_key.randint(0, self.queen_count-1))
        return board

    # Evaluates and returns the fitness of the board by assessing how many
    # collisions each queen encounters.
    # NOTE: A float of 0 means there were no collisions and it is a solution
    # NOTE: A float of 1 means there were maximal collisions
    def find_fitness(self):
        collisions = 0
        #Horizontal Detection
        for i in range(0, self.queen_count):
            j = (i+1) % self.queen_count
            while (i != j):
                if (self.board_key[i] == self.board_key[j]):
                    collisions += 1
                j = (j+1) % self.queen_count
        #Vertical Detection
        
        for i in range(0, self.queen_count):
            j = 1
            # -Up Right and Down Right 
            while (i+j < self.queen_count):
                test_key_up = int(self.board_key[i]) - j
                test_key_down = int(self.board_key[i]) + j
                if (int(self.board_key[i+j]) == test_key_up):
                    collisions += 1
                if (int(self.board_key[i+j]) == test_key_down):
                    collisions += 1
                j += 1
            # -Up Left and Down Left
            j = 1
            while (i-j >= 0):
                test_key_up = int(self.board_key[i]) - j
                test_key_down = int(self.board_key[i]) + j
                if (int(self.board_key[i-j]) == test_key_up):
                    collisions += 1
                if (int(self.board_key[i-j]) == test_key_down):
                    collisions += 1
                j += 1
        
        return (collisions / float(self.queen_count**2 - self.queen_count))

        

    #Prints out a visual representation of this board.
    def print_board(self):
        for y in range(0, self.queen_count):
            row = ""
            for x in range(0, self.queen_count):
                if (self.board_key[x] == str(y)):
                    row += "Q "
                else:
                    row += "- "
            print row

    
    

    
