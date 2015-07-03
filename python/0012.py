
from util import get_factors
from util import get_triangle_number

result = 0
i = 0
while True:
    i += 1
    x = get_triangle_number(i)
    factors = get_factors(x)
    if len(factors) >= 500:
        result = x
        break

print(result)

