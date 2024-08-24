def is_good_lab(n, grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 1:
                found = False
                for k in range(n):
                    for l in range(n):
                        if grid[i][j] == grid[i][k] + grid[l][j]:
                            found = True
                            break

                        if found:
                            break

                if not found:
                    return False
    return True


n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

if is_good_lab(n, grid):
    print("Yes")
else:
    print("No")
