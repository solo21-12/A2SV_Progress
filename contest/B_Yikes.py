
import bisect

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
jo = list(map(int, input().split()))
piles = [0, nums[0]]


for i in range(1, len(nums)):
    piles.append(piles[i] + nums[i])

for j in jo:
    print(bisect.bisect_left(piles, j))
