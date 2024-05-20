n, k = map(int, input().split())
nums_a = list(map(int, input().split()))
nums_b = list(map(int, input().split()))

nums_a.sort()
nums_b.sort()
N = len(nums_a)

def possible(curSum, k):
    j = N - 1
    count = 0

    for i in range(N):
        while j >= 0 and nums_a[i] + nums_b[j] > curSum:
            j -= 1

        count += (j + 1)

    return count >= k


low, high = nums_a[0] + nums_b[0], nums_a[-1] + nums_b[-1] + 1
while low < high:
    mid = (low + high) // 2

    if possible(mid, k):
        high = mid
    else:
        low = mid + 1


print(low)
