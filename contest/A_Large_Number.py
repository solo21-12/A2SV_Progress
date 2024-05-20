import bisect


def solve(nums, d, i):
    res = []

    for j in range(len(nums)):
        if j == i:
            res.append(str(d))

        res.append(str(nums[j]))

    if i == len(nums):
        res.append(str(d))

    return int("".join(res))


def findIndex(num, nums):
    for i in range(len(nums)):
        if num > nums[i]:
            return i

    return len(nums)


t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    num = list(map(int, input()))

    ans = float('-inf')
    ind = findIndex(d, num)
    ans = solve(num, d, ind)

    print(ans)
