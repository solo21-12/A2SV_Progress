s, b = map(int, input().split())
a = list(map(int, input().split()))

bases = []

for _ in range(b):
    d, g = map(int, input().split())
    bases.append([d, g])

bases.sort(key=lambda x: x[0])

prefix_sum = [0] * (b + 1)
for i in range(len(bases)):
    prefix_sum[i + 1] = prefix_sum[i] + bases[i][1]

def solve(bases, ship):
    low, high = 0, len(bases)

    while low < high:
        mid = (low + high) // 2

        if bases[mid][0] <= ship:
            low = mid + 1
        else:
            high = mid

    return low

for ship in a:
    i = solve(bases, ship)
    print(prefix_sum[i], end=" ")
