#!/usr/bin/python

#Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2
import board

queen_count = 4

#queen_count = int(raw_input("How many queens? \n"))
#if queen_count <= 0:
#    print 'Choose an integer greater than 0...'
#else:
myboard = board.NQueensBoard(queen_count)
myboard.print_queen_order()
myboard.print_board()
myboard.get_queen_fitness()
myboard.print_queen_order()

