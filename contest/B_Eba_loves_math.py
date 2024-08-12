t = int(input())


def solve(nums):

    res = 0

    for i in range(32):
        on = True
        for num in nums:

            if num & (1 << i) == 0:
                on = False

        if on:
            res ^= (1 << i)

    return res


for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    print(solve(nums))
