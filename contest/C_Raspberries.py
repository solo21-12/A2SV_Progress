def solve(nums, k):

    res = float('inf')

    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1

        if num % k == 0:
            res = 0
        else:
            res = min(res, k - (num % k))

    if k == 4:
        minn = max(0, 2 - count)
        res = min(minn, res)

    return res


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    ans = solve(nums, k)
    print(ans)
    