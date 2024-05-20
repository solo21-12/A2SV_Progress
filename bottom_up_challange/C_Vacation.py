from math import inf


n = int(input())

grid = []

for _ in range(n):
    nums = list(map(int, input().split()))
    grid.append(nums)


def solve(grid, n):
    prev = grid[-1]

    for i in range(n - 2, -1, -1):
        cur = [0 for _ in range(3)]

        for j in range(3):

            minn = 0

            for k in range(3):

                if k != j:
                    temp = grid[i][j] + prev[k]
                    minn = max(minn, temp)

            cur[j] = minn

        prev = cur

    return max(prev)


print(solve(grid, n))
