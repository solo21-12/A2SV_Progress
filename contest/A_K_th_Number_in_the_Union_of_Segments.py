def possible(num):
    cnt = 0
    for low, high in nums:
        if low < num:
            cnt += min(num - low, high - low + 1)

    return cnt <= k


n, k = map(int, input().split())
nums = []

for _ in range(n):
    a, b = map(int, input().split())
    nums.append([a, b])


low, high = -2 * pow(10, 9) - 1, 2 * pow(10, 9) + 1

while low < high:
    mid = (low + high) // 2

    if possible(mid):
        low = mid + 1
    else:
        high = mid

print(low - 1)
