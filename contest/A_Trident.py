from math import inf


def solve(nums, n):
    first, second = (inf, inf), (inf, inf)

    for i, num in enumerate(nums):
        if num < first[0]:
            first = (num, i + 1)
        elif second[0] != inf and num < second[0] and first[1] < second[1]:
            return [first[1], second[1], i + 1]
        else:
            second = (num, i + 1,)

    return []


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    

    ans = solve(nums, n)
    if ans:
        print("YES")
        print(*ans)
    else:
        print("NO")
