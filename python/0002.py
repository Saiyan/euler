#! /usr/bin/python

import util

n = 1
m = 2
temp = 0
sum_even = 0

while m < 4000000:
    if m % 2 == 0:
        sum_even += m
    temp = n+m
    n = m
    m = temp

print(sum_even)