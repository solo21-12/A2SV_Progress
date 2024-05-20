from math import inf


n, k = map(int, input().split())
nums = list(map(int, input().split()))


def solve(k, n):
    dp = [0 for _ in range(n)]

    for i in range(n - 2, -1, -1):
        cur_min = 10 ** 9

        for j in range(i + 1, min(n, i + k + 1)):
            cur = abs(nums[i] - nums[j]) + dp[j]
            cur_min = min(cur_min, cur)

        dp[i] = cur_min if cur_min != 10 ** 9 else 0

    return dp[0]


print(solve(k, n))
