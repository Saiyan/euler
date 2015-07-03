
from util import is_hexagonal_numver
from util import is_pentagon_number
from util import get_triangle_number

for i in range(286, 1000000):
    tri = get_triangle_number(i)
    if is_pentagon_number(tri) and is_hexagonal_numver(tri):
        print(tri)
        print(i)
        break