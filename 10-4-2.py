from functools import reduce

a = list(range(1,11))
n = reduce(lambda x, y: x* y, a)
print(n)
