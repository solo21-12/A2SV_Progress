n, k = map(int, input().split())
nums = list(map(int, input().split()))
queries = list(map(int, input().split()))


def solve(target):
    low, high = -1, len(nums)

    while low + 1 < high:
        mid = (low + high) // 2

        if nums[mid] <= target:
            low = mid
        else:
            high = mid
            
    return low + 1


for num in queries:
    print(solve(num))
    
