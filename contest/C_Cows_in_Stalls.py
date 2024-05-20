def possible(dist, cows, stalls):
    cnt = 1
    last = stalls[0]

    for i in range(1, len(stalls)):
        if abs(stalls[i] - last) >= dist:
            last = stalls[i]
            cnt += 1

    return cnt >= cows


n, k = map(int, input().split())
stalls = list(map(int, input().split()))
low, high = 0, max(stalls) + 1

while high > low + 1:
    mid = (low + high) // 2

    if possible(mid, k, stalls):
        low = mid
    else:
        high = mid


print(low)
