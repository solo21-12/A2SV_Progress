def solve(num, nums):
    low, high = 0, len(nums)

    while low < high:
        mid = (low + high) // 2

        if nums[mid] <= num:
            low = mid + 1
        else:
            high = mid

    return low


n = int(input())
nums = list(map(int, input().split()))
q = int(input())
nums.sort()

for _ in range(q):
    i = int(input())
    print(solve(i, nums))
