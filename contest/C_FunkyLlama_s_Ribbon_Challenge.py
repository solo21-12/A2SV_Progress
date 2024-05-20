
from math import e
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
import threading

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def solve(size, a, b, c, dp):
    if size == 0:
        return 0
    elif size < 0:
        return float('-inf')
    elif  size in dp:
        return dp[size]

    by_a = 1 + solve(size - a, a, b, c, dp)
    by_b = 1 + solve(size - b, a, b, c, dp)
    by_c = 1 + solve(size - c, a, b, c, dp)

    dp[size] = max(by_a, by_b, by_c)
    return dp[size]


def main():
    n, a, b, c = map(int, input().split())
    dp = defaultdict(int)

    print(solve(n, a, b, c, dp))


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
