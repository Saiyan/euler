
from util import is_prime

def is_truncatable_prime(string, left):
    n = int(string)
    if is_prime(n):
        if n < 10:
            return True
        else:
            next = string[0:-1]
            if left:
                next = string[1::]
            return is_truncatable_prime(next, left)
    else:
        return False


trunc_sum = 0
max = 11
i = 10
while max > 0:
    i += 1
    if is_truncatable_prime(str(i), True) and is_truncatable_prime(str(i), False):
        trunc_sum += i
        max -= 1
        print(i)

print(trunc_sum)