
from util import is_pentagon_number
from util import get_pentagonal_number

i = 0

print("generate pentagons...")
pentagons = []
for i in range(1, 10000):
    pentagons.append(get_pentagonal_number(i))
print("done!")


D=0
is_break = False
for j in pentagons:
    if is_break: break
    for k in pentagons:
        summ = j+k
        diff = j > k and j-k or k-j

        if is_pentagon_number(summ) and is_pentagon_number(diff):
            D = diff
            is_break = True
            break
print(D)


