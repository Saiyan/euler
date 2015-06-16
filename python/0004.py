#! /usr/bin/python

import util

largest_palindrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i * j
        if util.is_palindrome(str(prod)) and prod > largest_palindrome:
            largest_palindrome = prod

print(largest_palindrome)

