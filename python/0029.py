
from math import pow

results = []

for a in range(2, 101):
    for b in range(2, 101):
        res = pow(a, b)
        if not res in results:
            results.append(res)

print(len(results))