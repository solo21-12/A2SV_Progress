

n, a, b = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

print(nums[b] - nums[:b][-1])
