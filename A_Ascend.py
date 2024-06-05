n = int(input())
nums = list(map(int, input().split()))


def solve():
    count = 0
    cur = 1

    last = nums[0]

    for r in range(1, n):
        if last >= nums[r]:
            last = 0
            cur = 0
            
        cur += 1
        last = nums[r]
        count = max(count, cur)

    return count


print(solve())
