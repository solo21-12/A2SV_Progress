from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
import threading

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def is_palindrom(num):
    temp = num
    new_num = 0

    while num:
        new_num = new_num * 10 + num % 10
        num //= 10

    return temp == new_num


def solve(num, start, dp):
    # print(num)
    if num == 0:
        return 1
    elif num < 0:
        return 0
    elif (num, start) in dp:
        return dp[(num, start)]

    count = 0
    if is_palindrom(start) and start <= num:
        count += solve(num - start, start, dp)

    if start + 1 <= num:
        count += solve(num, start + 1, dp)

    dp[(num, start)] = count

    return dp[(num, start)]


def solve_bottom_up(num):
    start = num
    dp = [[0 for _ in range(start + 1)] for _ in range(num + 1)]

    for i in range(num + 1):
        dp[0][i] = 1
        
    # print(dp)
    for n in range(1, num + 1):
        for start in range(1, n):
            count = 0
            if is_palindrom(start) and start <= n:
                count += dp[n - start][start]
                print(dp[n - start][start], start, n)

            # if start + 1 <= n:
            #     i
            #     count += dp[n][start + 1]
            # print(count)
            dp[n][start] = count if count > 0 else 0
            
    # print(dp)
    return dp[1][1]


def main():
    MOD = (10 ** 9) + 7
    t = int(input())

    for _ in range(t):
        n = int(input())
        dp = defaultdict(int)
        res = solve(n, 1, dp)
        res = res % MOD
        # print(res)
        print(solve_bottom_up(n))


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()


'''
[[1, 1, 1, 1, 1, 1],
[-1, -1, -1, -1, -1, -1], 
[-1, -1, -1, -1, -1, -1], 
[-1, -1, -1, -1, -1, -1], 
[-1, -1, -1, -1, -1, -1], 
[-1, -1, -1, -1, -1, -1]]

'''