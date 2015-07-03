
import util

curious_sum = 0

for i in range(3, 5000000):
    if util.is_curious(i):
        curious_sum += i

print(curious_sum)

