from collections import defaultdict


def is_almost(num):
    factors = set()
    d = 2

    while d * d <= num:

        while not num % d:
            factors.add(d)
            num //= d

        d += 1

    if num > 1:
        factors.add(num)

    return len(factors) == 2


n = int(input())
cnt = 0
for num in range(1, n + 1):
    if is_almost(num):
        cnt += 1

print(cnt)
