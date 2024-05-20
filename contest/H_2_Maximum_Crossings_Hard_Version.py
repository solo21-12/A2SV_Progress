from typing import List
import bisect

class Solution:
    def solve(self, nums: List[int]):
        def count(left_half, right_half):
            nonlocal cost
            for num in right_half:
                r = bisect.bisect_left(left_half, num)
                cost += len(left_half) - r
                

        def merge(left_half, right_half):
            l, r = 0, 0
            sorted_array = []

            while l < len(left_half) and r < len(right_half):
                if left_half[l] <= right_half[r]:
                    sorted_array.append(left_half[l])
                    l += 1
                else:
                    sorted_array.append(right_half[r])
                    r += 1

            sorted_array.extend(left_half[l:])
            sorted_array.extend(right_half[r:])

            return sorted_array

        def merge_sort(left, right):
            if left == right:
                return [nums[left]]

            mid = (left + right) // 2

            left_half = merge_sort(left, mid)
            right_half = merge_sort(mid + 1, right)

            count(left_half, right_half)

            return merge(left_half, right_half)

        cost = 0
        merge_sort(0, len(nums) - 1)

        return cost
    


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    solution = Solution()
    ans = solution.solve(nums)
    print(ans)