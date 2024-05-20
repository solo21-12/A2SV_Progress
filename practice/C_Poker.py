from heapq import heappush, heappop


def solve(nums):
    heap = []
    count = 0
    for n in nums:
        if n > 0:
            heappush(heap, -n)
        else:
            if heap:
                maxx = heappop(heap)
                count += (-maxx)

    return count


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    print(solve(nums))
