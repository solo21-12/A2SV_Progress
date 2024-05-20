# # n = int(input())
# import threading

# threading.stack_size(1 << 27)
# main_thread = threading

def nSum(n):
    if n == 1:
        return 1

    return n + nSum(n - 1)


# print(nSum(n))


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


# print(factorial(n))

def reverseArray(l, r, nums):
    if l == r:
        return

    nums[l], nums[r] = nums[r], nums[l]

    return reverseArray(l + 1, r - 1, nums)


def reverseArrayInOne(nums, l):
    N = len(nums)
    if l > N // 2:
        return
    
    nums[l], nums[N - l - 1] = nums[N - 1 - l], nums[l]

    return reverseArrayInOne(nums, l + 1)


nums = list(map(int, input().split()))
l, r = 0, len(nums) - 1

reverseArrayInOne(nums, l)

print(nums)
