from math import inf
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
import threading

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def solve(i, j, dp, row, col, k):
    if (i, j) == (row - 1, col - 1) and k == 0:

        return True
    elif i >= row or j >= col:
        return False
    elif dp[i][j] != -1:
        return dp[i][j]

    right = solve(i, j + 1, dp, row, col, k - (i + 1))
    bottom = solve(i + 1, j, dp, row, col, k - (j + 1))
    dp[i][j] = right or bottom
    return dp[i][j]


def main():
    t = int(input())
    for _ in range(t):
        row, col, k = map(int, input().split())

        dp = [[-1 for _ in range(col + 1)] for _ in range(row + 1)]

        min_cost = solve(0, 0, dp, row, col, k)
        # print(min_cost)
        if min_cost:
            print("YES")
        else:
            print("NO")


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
