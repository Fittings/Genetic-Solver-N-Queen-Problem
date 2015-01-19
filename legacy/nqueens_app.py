#!/usr/bin/python

#Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2

import evolver

population = 40
queen_count = 8


sol_count = int(raw_input(
    "How many times will we run the %d-queens solution finder?\n" % queen_count))

i = 0
epochs_list = []
total_epochs = 0
best_fitness_generation_list = []

for i in range(0, sol_count):
    print 'Finding a solution for %d queen problem...\n' % queen_count
    epochs = 0
    solution = evolver.Evolver(population, queen_count)
    restart_flag = solution.evolve_board()
    epochs += solution.epochs
    while not(restart_flag):
        solution = evolver.Evolver(population, queen_count)
        restart_flag = solution.evolve_board()
        epochs += solution.epochs
    total_epochs += epochs
    epochs_list.append(epochs)
    best_fitness_generation_list = solution.best_generation_list
    print '\nDone! This took %d epochs' % epochs_list[i]
    
        
epochs_list = sorted(epochs_list)
average = round(total_epochs / float(i+1))
lowest = epochs_list[0]
highest = epochs_list[len(epochs_list)-1]

file = open('solution_info', 'w')
for i in range(0, len(best_fitness_generation_list)):
    file.write(str(i)+"\t" + str(best_fitness_generation_list[i].fitness)+"\n") 



print "~~~~~~~~~~~~~~~~"
#print "There were on average %d repopulations." % average

