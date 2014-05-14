#!/usr/bin/python

#Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import evolver

sol_count = int(raw_input(
    "How many times will we run the n-queens solution finder?\n"))

i = 0
epochs = 0
while (i < sol_count):
    solution = evolver.Evolver(10, 8)
    epochs += solution.evolve_board()
    i += 1

average = round(epochs / float(i))
print "~~~~~~~~~~~~~~~~"
print "There were on average %d epochs" % average
