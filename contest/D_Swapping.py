t = int(input())

for _ in range(t):
    n, x, m = map(int, input().split())
    left = right = x

    for _ in range(m):
        l, r = map(int, input().split())
        if l <= left <= r or l <= right <= r:
            left = min(left, l)
            right = max(right, r)

    print(right - left + 1)