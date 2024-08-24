from math import inf
from email.policy import default
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
import threading

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def solve(num, dp):
    if num < 1:
        return inf
    elif num == 1:
        return 0
    elif dp[num] > 0:
        return dp[num]

    two = inf
    three = inf
    five = inf
    if not num % 2:
        two = solve(num // 2, dp)
    elif not num % 3:
        three = solve((num * 2) // 3, dp)
    elif not num % 5:
        five = solve((num * 4) // 5, dp)

    dp[num] = min(two, three, five) + 1

    return dp[num]


def main():
    dp = defaultdict(int)

    for _ in range(int(input())):
        n = int(input())

        n = solve(n, dp)

        if n == inf:
            print(-1)
        else:
            print(n)
    pass


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
