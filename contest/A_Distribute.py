n = int(input())
nums = list(map(int, input().split()))


def solve(nums):
    nums = [(num, i + 1) for i, num in enumerate(nums)]
    nums.sort()

    l, r = 0, len(nums) - 1

    while l < r:
        print(nums[l][1], nums[r][1])

        l += 1
        r -= 1


solve(nums)
