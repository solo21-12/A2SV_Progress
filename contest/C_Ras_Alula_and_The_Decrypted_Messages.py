def solve(s, target, m):
    cnt = 0
    cost = 0
    l = 0
    for r in range(len(s)):
        cost += ord(s[r])

        if r - l + 1 == m:
            if cost == target:
                return True

            cost -= ord(s[l])
            l += 1

    return False


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    target = input()
    c = 0
    for t in target:
        c += ord(t)

    ans = solve(s, c, m)
    if ans:
        print("YES")
    else:
        print("NO")
