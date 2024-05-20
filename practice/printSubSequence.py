from typing import List


nums = [3, 1, 2,2,1]
ans = []


def printSequence(i, arr: List[int]):
    global nums, ans
    N = len(nums)

    if i >= N:
        # num = arr.copy()
        ans.append(arr)

        return

    arr.append(nums[i])
    printSequence(i + 1, arr)
    arr.remove(nums[i])
    printSequence(i + 1, arr)


printSequence(0, [])


# print(ans)

def reverse(nums):
    nums[:] = nums[::-1]
    # This is creating a new memory address and make a reference to that
    # print(nums)


my_list = [1, 2, 3]
reverse(my_list)
# print(my_list)


def subseuenceSumK(i, arr: List[int], currSum, k):
    global nums

    N = len(nums)

    if i >= N:
        if currSum == k:
            print(arr)
        
        return


    arr.append(nums[i])
    currSum += nums[i]
    subseuenceSumK(i + 1, arr, currSum, k)

    arr.pop()
    currSum -= nums[i]
    subseuenceSumK(i + 1, arr, currSum, k)


subseuenceSumK(0, [], 0, 5)

