from math import ceil


def multiple_of(n, m):
    if m % n == 0:
        return True
    return False

def is_prime(n):
    if(n == 2): return True
    max = ceil(n/2)
    for i in range(2,max):
        if n % i == 0:
            return False
    return True

def is_palindrome(string):
    string_reversed = string[::-1]
    for c in range(0, len(string)):
        if string_reversed[c] != string[c]:
            return False
    return True






