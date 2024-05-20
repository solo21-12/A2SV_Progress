import re
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
import threading
from typing import Counter

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def solve(idx, dp, counter):
    if idx > (10 ** 5) + 1:
        return 0
    elif idx in dp:
        return dp[idx]

    inc = counter[idx] + solve(idx + 2, dp, counter)
    exc = solve(idx + 1, dp, counter)

    dp[idx] = max(inc, exc)
    return dp[idx]


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    counter = [0] * (10 ** 5 + 7)
    dp = defaultdict(int)

    for num in nums:
        counter[num] += num

    print(solve(0, dp, counter))


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
