def solve(l, r, d):
    a = (l // d)
    b = (r // d) + 1

    if d < l:
        return d

    return b * d


for _ in range(int(input())):

    l, r, d = map(int, input().split())

    print(solve(l, r, d))
