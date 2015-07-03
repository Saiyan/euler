
from util import is_palindrome

pali_sum = 0
for i in range(1, 1000000):
    str_bin = str(bin(i)).lstrip("0b")
    str_10 = str(i)
    if is_palindrome(str_10) and is_palindrome(str_bin):
        print(str_bin,str_10)
        pali_sum += i

print(pali_sum)