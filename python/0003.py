#! /usr/bin/python

import util
import math

largest_prime_factor=0
num = 600851475143
max = math.floor(num/2)
for i in reversed(range(2, max)):
    if num % i == 0 and util.is_prime(i):
        largest_prime_factor = i
        break

print(largest_prime_factor)
