
from util import is_pandigital
from itertools import permutations

print("generate  pandigitals...")
pandigitals = permutations("0123456789", 10)
print("done!")


pan_sum = 0
for p in pandigitals:
    strp = "".join(p)
    if strp[0] == "0":
        continue

    d234 = int("{}{}{}".format(p[1], p[2], p[3]))
    d345 = int("{}{}{}".format(p[2], p[3], p[4]))
    d456 = int("{}{}{}".format(p[3], p[4], p[5]))
    d567 = int("{}{}{}".format(p[4], p[5], p[6]))
    d678 = int("{}{}{}".format(p[5], p[6], p[7]))
    d789 = int("{}{}{}".format(p[6], p[7], p[8]))
    d890 = int("{}{}{}".format(p[7], p[8], p[9]))

    if d234 % 2 != 0:
        continue
    if d345 % 3 != 0:
        continue
    if d456 % 5 != 0:
        continue
    if d567 % 7 != 0:
        continue
    if d678 % 11 != 0:
        continue
    if d789 % 13 != 0:
        continue
    if d890 % 17 != 0:
        continue

    pan_sum += int(strp)

print(pan_sum)
