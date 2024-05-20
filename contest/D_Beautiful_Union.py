from collections import defaultdict


def solve(nums1, nums2):
    countNums1 = defaultdict(int)
    countNums2 = defaultdict(int)

    i = 0

    while i < len(nums1):
        c = i
        while c < len(nums1) and nums1[c] == nums1[i]:
            c += 1

        countNums1[nums1[i]] = max(c - i, countNums1[nums1[i]])
        i = c

    i = 0

    while i < len(nums2):
        c = i
        while c < len(nums2) and nums2[c] == nums2[i]:
            c += 1

        countNums2[nums2[i]] = max(c - i, countNums2[nums2[i]])
        i = c
    ans = 0
    for num in nums1:
        ans = max(ans, countNums1[num] + countNums2[num])

    for num in nums2:
        ans = max(ans, countNums1[num] + countNums2[num])


    return ans




t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(solve(a, b))
