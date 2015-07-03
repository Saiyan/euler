from math import pow

sum_all = 0

for i in range(2, 1000000):
    temp = 0
    for c in str(i):
        temp += pow(int(c), 5)
    if temp == i:
        sum_all += i

print(sum_all)