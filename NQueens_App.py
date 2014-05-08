#!/usr/bin/python

#Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2
import NQueens


queen_count = int(raw_input("How many queens? \n"))
if queen_count <= 0:
    print 'Choose an integer greater than 0...'
else:
   myboard = NQueens.NQueens(queen_count)
   myboard.print_board()

