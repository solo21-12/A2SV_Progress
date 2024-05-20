w, h, n = map(int, input().split())


def good(x):
    return (x // h) * (x // w) >= n


l = 0
r = 1

while not good(r):
    r *= 2

while r > l + 1:
    mid = (l + r) // 2

    if good(mid):
        r = mid
    else:
        l = mid


print(r)
