#!/usr/bin/python

#Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import evolver

population = 10
queen_count = 8


sol_count = int(raw_input(
    "How many times will we run the single crossover %d-queens solution finder?\n" % queen_count))




i = 0
total_epochs = 0
epochs_list = []

while (i < sol_count):
    solution = evolver.Evolver(population, queen_count)
    epochs = solution.evolve_board()
    total_epochs += epochs
    epochs_list.append(epochs)
    i += 1
epochs_list = sorted(epochs_list)
average = round(total_epochs / float(i))
lowest = epochs_list[0]
highest = epochs_list[len(epochs_list)-1]
file = open('singlecrossover', 'w')
file.write("#####\n")
file.write("average: " + str(average))
file.write("\n#####\n")
file.write("lowest: " + str(lowest))
file.write("\n#####\n")
file.write("highest: " + str(highest))
file.write("\n#####\n")
file.write(str(epochs_list))
file.write("\n#####\n")


print "~~~~~~~~~~~~~~~~"
print "There were on average %d epochs" % average
