import bisect

n = int(input())
nums = list(map(int, input().split()))
k = int(input())
nums.sort()

for _ in range(k):
    l,  r = map(int, input().split())

    ls = bisect.bisect_left(nums, l)
    rs = bisect.bisect_right(nums, r)

    print(rs - ls, end=" ")
