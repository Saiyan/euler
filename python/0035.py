
from util import is_circular_prime
from util import is_prime

count = 0
for i in range(2, 1000000):
    if is_circular_prime(i):
        count += 1

print(count)