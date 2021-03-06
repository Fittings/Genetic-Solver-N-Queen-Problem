#!/usr/bin/python

# Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import random
import queen

class NQueensBoard:
    'This class is used to create a n x n chessboard and ' \
        '"evolve" a non-conflicting solution of Queen Placements'

        
    # Initializes a board with n Queens in random positions
    def __init__(self, queen_count=0):
        self.queen_count = queen_count
        self.random_set_up()

    # Sets the board with queens placed on every column with random
    # row positions. Also initializes the queen 'priority' list
    def random_set_up(self):
        print "\nThis is the %d-Queen problem!\n" % self.queen_count
        self.board = []
        self.queen_priority = []
        for x in range(0, self.queen_count):
            x_list = [] #The '2d' part of the list
            queen_key = self.generate_position_key()   
            queen_y = self.get_position(queen_key) #y-coord of the queen
            for y in range(0, self.queen_count):
                if (y == queen_y):
                    temp_queen = queen.Queen(x, queen_y, queen_key)
                    x_list.append(queen)
                    self.queen_priority.append(temp_queen)
                else:
                    x_list.append("0")
            self.board.append(x_list)

    #ZZZ ZZZ This has an easy fix, dont do whatever I was doing, and just mod...
    #ZZZ we have a magic number in determining the length of the key. This
    #ZZZ length may be a fix to some issues for me.
    # Generates a random int and returns as a string to represent the queens
    # row position on the board.
    def generate_position_key(self):
        random_key = random.SystemRandom()
        position_key = random_key.randint(0, 100 ** self.queen_count)
        return str(position_key)
        

    # Returns the position of the queen in the given column.
    def get_position(self, position_key):
        temp_string = position_key
        queen_count_length = str(self.queen_count)
        while (len(temp_string) > len(queen_count_length)):
            temp_int = 0
            for i in range(0, len(temp_string)):
                temp_int += int(temp_string[i])
        
            temp_string = str(temp_int)
        return int(temp_string) % self.queen_count

    #ZZZ This is pointless. Needs to be removed ;(
    # Makes a list of the queens in order of fitness. 
    def set_queen_priorities(self):
        total_fitness = 0
        for i in range(0, self.queen_count):
            best_queen = self.queen_priority[i]
            for j in range(0, self.queen_count):
                if (self.queen_priority[i].fitness
                    < self.queen_priority[j].fitness):
                    self.queen_priority[i] = self.queen_priority[j]
                    self.queen_priority[j] = best_queen
                    best_queen = self.queen_priority[i]
                    
                    
                
            
    #ZZZ Collision detecting is working! :)
    # Returns the number of collisions with other queens based on possible queen
    # movement
    def get_board_fitness(self):
        for i in range(0, self.queen_count):
            test_queen = self.queen_priority[i]
            queen_collisions = 0
            

            #Test Horizontal #ZZZ Works!
            x = (test_queen.x_position +1) % self.queen_count
            y = test_queen.y_position
            while (x != test_queen.x_position):
                if (self.board[x][y] != "0"):
                    queen_collisions += 1
                x = (x+1) % self.queen_count
            
            #Test Diagonal up right #ZZZ Works!
            x = test_queen.x_position
            y = test_queen.y_position
            while True:
                x += 1
                y -= 1
                if (x > (self.queen_count-1) or y < 0):
                    #This allows us to loop diagonally.
                    temp = x-1
                    x = y+1
                    y = temp
                if (x == test_queen.x_position):
                    #If we arrive at origin position, break loop
                    break
                if (self.board[x][y] != "0"):
                    queen_collisions += 1
            #Test Diagonal down right #ZZZ Works!
            x = test_queen.x_position
            y = test_queen.y_position
            while True:
                x += 1
                y += 1
                if (x > (self.queen_count-1)):
                    #This allows us to loop diagonally.
                    x = x-y
                    y = 0
                if (y > (self.queen_count-1)):
                    #This allows us to loop diagonally.
                    y = y-x
                    x = 0
                if (x == test_queen.x_position):
                    #If we arrive at origin position, break loop
                    break
                if (self.board[x][y] != "0"):
                    queen_collisions += 1
                        
            #Give our queen her fitness count
            test_queen.set_fitness(float(queen_collisions) / self.queen_count)
        self.set_queen_priorities()
        return queen_collisions


    #ZZZ Completely pointless, needs to be removed~
    # This will use cross-over and mutation to create new queen positions
    # for the 'unfit' queens
    def evolve_queens(self):
        #use the strong queens to replace the week queens
        pass
                    
            
    #ZZZ Completely pointless, needs to be removed.
    def queen_crossover(self, queen1, queen2):
        crossover_point = random_key.randint(0, len(queen1.y_key))
        new_key = queen1.y_key[:crossover_point]
        new_key += queen2.y_key[crossover_point:]
        return new_key
        
        



        

    #====Prints====#
        
            

        
    # Prints the queens in order of current priority.
    def print_queen_order(self):
        for i in range(0, self.queen_count):
            print("[%d]Queen: " % i),
            self.queen_priority[i].print_queen()

    
    # Prints a visual-representation of the board and queens
    def print_board(self):
        for y in range(0, self.queen_count):
            row_string = '    '
            for x in range(0, self.queen_count):
                if (self.board[x][y] == "0"):
                    row_string += '- '
                else:
                    row_string += 'Q '
            print row_string
        print 
                    



