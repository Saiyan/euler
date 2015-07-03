from math import ceil
from math import sqrt
from math import factorial


def multiple_of(n, m):
    if m % n == 0:
        return True
    return False

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    max = ceil(sqrt(n))
    for i in range(2, max+1):
        if n % i == 0:
            return False
    return True



def is_circular_prime(n):
    def get_rotations(strn):
        def nextRotation(strn):
            r = ""
            for i in range(1,len(strn)):
                r += strn[i]
            r += strn[0]
            return r
        rot = []
        for c in strn:
            strn = nextRotation(strn)
            rot.append(strn)
        return rot

    strn = str(n)
    for r in get_rotations(strn):
        if not is_prime(int(r)):
            return False
    return True

def is_palindrome(string):
    string_reversed = string[::-1]
    for c in range(0, len(string)):
        if string_reversed[c] != string[c]:
            return False
    return True

def get_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

def get_triangle_number(n):
    return int(0.5*n*(n+1))

def is_triangle_number(n):
    x = (sqrt(8 * n + 1) - 1) / 2
    return str(x).endswith(".0")

def is_hexagonal_numver(n):
    x = (sqrt(8 * n +1) + 1) / 4
    return str(x).endswith(".0")

def is_curious(n):
    strnr = str(n)
    sum_n = 0
    for c in strnr:
        i = int(c)
        sum_n += factorial(i)
    if n == sum_n:
        return True
    else:
        return False

def is_pandigital(n, start=0, stop=9):
    strn = str(n)
    for i in range(start, stop+1):
        strn = str(n)
        temp = []
        for c in strn:
            i = int(c)
            if i < start or i > stop or i in temp:
                return False
            temp.append(i)
        return True

def get_integer_value_from_char(c):
    cl = c.lower()
    return char_values[cl];

char_values = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}

def get_pentagonal_number(n):
    return int(n * (3*n - 1) / 2)

def is_pentagon_number(n):
    x = (sqrt(24*n+1)+1) / 6
    if str(x).endswith(".0"):
        return True
    return False