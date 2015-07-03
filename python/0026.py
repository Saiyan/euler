__author__ = 'christian.sucker'

from mpmath import mpf
from mpmath import mp

longest_cycle = ""
digit = 0

for i in range(2, 1000):
    mp.dps = 50
    val = mpf(1)/i
    strval = str(val).rstrip('0').lstrip('0.')

    for j in range(0, len(strval)):
        temp = ""
        last = ""
        for k in range(j, len(strval)):
            temp += strval[k]
            if strval.index(temp) >= 0 and strval[k] != last:
                last = strval[k]
                if len(temp) > len(longest_cycle):
                    longest_cycle = temp
                    digit = i
                continue
            else:
                break

print(longest_cycle, digit,)