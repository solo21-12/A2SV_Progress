n, k = map(int, input().split())
nums = list(map(int, input().split()))

res = 0
for num in nums:
    c = 0
    for ch in str(num):
        if ch == '4' or ch == '7':
            c += 1

    if c <= k:
        res += 1

print(res)
