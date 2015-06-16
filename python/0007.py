#! /usr/bin/python

import util

count=0
prime = 0
for i in range(2, 999999999):
    if util.is_prime(i):
        prime = i
        count += 1
    if count == 10001:
        break

print(prime)
