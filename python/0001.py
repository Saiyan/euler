#! /usr/bin/python

import util

sum_multiples=0

for i in range(1,999):
    if util.multiple_of(3, i) or util.multiple_of(5,i):
        sum_multiples+=i

print(sum_multiples)
