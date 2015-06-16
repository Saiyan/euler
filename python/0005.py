#! /usr/bin/python

import util

largest_num = 0
i=200000000
while(True):
    i += 1
    for j in range(1, 21):
        if not i % j == 0:
            break
        if j == 20:
            largest_num = i
    if largest_num > 0:
        break

print(largest_num)
