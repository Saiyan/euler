
def is_pandigital(n):
    sn = str(n)
    if len(sn) != 9 or "0" in sn:
        return False
    temp = ""
    for c in sn:
        if c in temp:
            return False
        temp += c
    return True


def concatenated_product(n, arr):
    prod_str = ""
    for i in arr:
        prod_str += str(n * i)
    return prod_str

largest = 0

for i in range(1, 10000):
    for n in range(2, 100):
        prod = concatenated_product(i, range(1, n))
        iprod = int(prod)
        if is_pandigital(iprod) and iprod > largest:
            largest = iprod
            print(largest)

print(largest)