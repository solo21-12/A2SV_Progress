n, k = map(int, input().split())
nums = list(map(int, input().split()))
querie = list(map(int, input().split()))


def solve(target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


for q in querie:
    if solve(q):
        print("YES")
    else:
        print("NO")
