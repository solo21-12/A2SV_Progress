from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
import threading

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def solve_bottom_up(nums):
    N = len(nums)
    dp = [0] * len(nums)
    dp[-1] = nums[-1]

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] + i <= N - 1:
            dp[i] = dp[i + nums[i]] + nums[i]
        else:
            dp[i] = nums[i]

    return max(dp)


def solve(idx, nums, dp):
    if idx >= len(nums):
        return 0
    elif dp[idx] != -1:
        return dp[idx]

    with_current = nums[idx] + solve(idx + nums[idx], nums, dp)
    dp[idx] = with_current
    return with_current


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        dp = [-1] * (n + 1)
        result = 0
        for i in range(n):
            result = max(result, solve(i, nums, dp))

        print(solve_bottom_up(nums))
    pass


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
