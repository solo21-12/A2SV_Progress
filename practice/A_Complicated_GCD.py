from functools import reduce

def solve(a, b):
    if a == b:
        return a

    return 1

a, b = map(int, input().split())
print(solve(a, b))
