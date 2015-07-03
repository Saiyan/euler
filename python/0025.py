__author__ = 'christian.sucker'

f1 = 1
f2 = 1
temp = 0
count = 2
for i in range(0, 25000):
    temp = f1
    f1 = f2
    f2 = temp + f1
    count += 1

    if len(str(f2)) >= 1000:
        break

print(count)

