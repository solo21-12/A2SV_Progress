

def is_possible(summ, nums, k):
    cnt = 1
    cur = 0

    for num in nums:
        cur += num
        if cur > summ:
            cnt += 1
            cur = num

    return cnt <= k


n, k = map(int, input().split())
nums = list(map(int, input().split()))


low, high = max(nums) - 1, sum(nums) + 1

while  high > low + 1:
    mid = (low + high) // 2

    if is_possible(mid, nums, k):
        high = mid
    else:
        low = mid

print(high)
