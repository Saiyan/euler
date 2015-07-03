
from util import is_prime

def is_pandigital(n):
    if n < 10: return False
    strn = str(n)
    max_digit = len(strn)
    temp = []
    for c in strn:
        i = int(c)
        if i == 0 or i > max_digit or i in temp:
            return False
        temp.append(i)
    return True

largest = 0

for x in range(2143, 987654321):
    if is_pandigital(x) and is_prime(x) and x > largest:
        largest = x

print(largest)

