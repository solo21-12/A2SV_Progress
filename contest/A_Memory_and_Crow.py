t = int(input())
nums = list(map(int, input().split()))

res = [0 for _ in range(t)]
res[-1] = nums[-1]


evens = 0
odds = 0

if (t - 1) % 2:
    odds += nums[-1]
else:
    evens += nums[-1]

for i in range(t - 2, -1, -1):
    cur = 0
    if i % 2:
        cur = nums[i] + evens - odds
        odds += cur
    else:
        cur = nums[i] - evens + odds
        evens += cur

    res[i] = cur


print(*res)
