t = int(input())


def solve(num, k):
    maxx = 0
    for num in nums:
        maxx = max(maxx, num | k)

    return maxx


for _ in range(t):
    n, z = map(int, input().split())
    nums = list(map(int, input().split()))

    print(solve(nums, z))
