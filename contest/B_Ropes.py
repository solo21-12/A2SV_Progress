n, k = map(int, input().split())


rope = []
for _ in range(n):
    rope.append(int(input()))


def count(x):
    cnt = 0

    for r in rope:
        cnt += (r // x)

    return cnt >= k


l, r = 0, 1e8
for _ in range(100):
    mid = (l + r) / 2

    if count(mid):
        l = mid
    else:
        r = mid


print(l)
