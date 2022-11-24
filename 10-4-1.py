from functools import reduce

a = list(range(1,101))
n = reduce(lambda x, y: x + y, a)
print(n)
