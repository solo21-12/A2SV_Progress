from typing import List


class Solution:
    def solve(self, nums: List[int]):
        def sort_single(arr):
            nonlocal cnt
            if arr[0] >= arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
                cnt += 1

        def merge(left_half, right_half):
            nonlocal cnt
            sorted_array = []
            if left_half[0][0] <= right_half[0][0]:
                sorted_array.extend(left_half)
                sorted_array.extend(right_half)
            else:
                cnt += 1
                sorted_array.extend(right_half)
                sorted_array.extend(left_half)

            return sorted_array

        def merge_sort(left, right):

            if left == right:
                sort_single(nums[left])
                return [nums[left]]

            mid = (left + right) // 2

            left_half = merge_sort(left, mid)
            right_half = merge_sort(mid + 1, right)

            return merge(left_half, right_half)

        cnt = 0
        res = merge_sort(0, len(nums) - 1)

        for i in range(len(res) - 1):
            if res[i][1] > res[i + 1][0]:
                return -1

        return cnt

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    if n <= 1:
        print(0)
        continue

    arr = [[nums[i], nums[i+1]] for i in range(0, len(nums) - 1, 2)]
    solution = Solution()
    print(solution.solve(arr))
