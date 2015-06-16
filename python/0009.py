#! /usr/bin/python

from math import pow

prod=0
break_loops=False
for i in range(1, 1000):
    for j in range(1, 1000):
        for k in range(1, 1000):
            if k < j < i and pow(k, 2) + pow(j, 2) == pow(i, 2) and k+j+i == 1000:
                prod = k*j*i
                break_loops = True
                break
        if break_loops:
            break
    if break_loops:
        break

print(prod)
