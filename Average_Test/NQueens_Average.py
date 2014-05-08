#!/usr/bin/python

#Cameron Milsom - May 2014
# n-Queen Problem - cosc343 assignment 2
import NQueens

queen_count = 1000

eight = NQueens.NQueens(queen_count)
sum = 0
count = 0
stand_count = 0
stand_sum = 0
while count <= 10000:
    if stand_count < queen_count:
        stand_sum += stand_count
        stand_count +=1
    else:
        stand_count = 1
    key = eight.generate_position_key()
    sum += eight.get_position(key)
    count += 1




average = sum / count
stand_average = stand_sum / count
#eight.print_board()
print 'The average y value was %d' % average
print 'The standard average y value was %d' % stand_average

