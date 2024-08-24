

from collections import defaultdict
from math import inf


def solve(init, fina):

    count = defaultdict(int)

    for i, ch in enumerate(init):
        count[ch] = max(count[ch], i)

    last = -1

    for ch in fina:
        print(count[ch], last)
        if count[ch] >= last:
            last = count[ch]
        else:
            return False

    return True


for _ in range(int(input())):

    a, b = input().split()

    if solve(a, b):
        print("YES")
    else:
        print("NO")
