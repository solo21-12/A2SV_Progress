from math import inf


n = int(input())
nums = list(map(int, input().split()))


def solve():
    dp = [0 for _ in range(n)]

    for i in range(n - 2, -1, -1):
        one = abs(nums[i] - nums[i + 1]) + dp[i + 1]
        two = 10 ** 9

        if i < n - 2:
            two = abs(nums[i] - nums[i + 2]) + dp[i + 2]

        dp[i] = min(one, two)

    return dp[0]


print(solve())
