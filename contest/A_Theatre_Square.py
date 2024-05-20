import math
n, m, a = map(int, input().split())

def least_flagstones(n, m, a):
    rows = math.ceil(n / a)
    columns = math.ceil(m / a)
    total = rows * columns
    return total


print(least_flagstones(n, m, a))
