n, m = map(int, input().split())
nums1 = list(map(int, input().split()))
nums = list(map(int, input().split()))
result = []
l, r = 0, 0
while l < n and r < m:
    if nums1[l] <= nums[r]:
        result.append(nums1[l])
        l += 1
    else:
        result.append(nums[r])
        r += 1

result.extend(nums1[l:])
result.extend(nums[r:])

print(*result)
