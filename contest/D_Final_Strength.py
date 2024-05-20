from typing import List
import bisect


class Solution:
    def solve(self, arr):
        def count(left_half, right_half):
            r = 0
            for i, (num, cnt) in enumerate(left_half):

                while r < len((right_half)) and num > right_half[r][0]:
                    r += 1

                left_half[i][1] += r
            l = 0

            for i, (num, cnt) in enumerate(right_half):

                while l < len((left_half)) and num > left_half[l][0]:
                    l += 1

                right_half[i][1] += l
                

            for i, (num, cnt) in enumerate(left_half):
                left_half[i][0] += cnt
                left_half[i][1] = 0

            for i, (num, cnt) in enumerate(right_half):
                right_half[i][0] += cnt
                right_half[i][1] = 0

        def merge(left_half, right_half):
            l, r = 0, 0
            sorted_array = []

            while l < len(left_half) and r < len(right_half):
                if left_half[l][0] <= right_half[r][0]:
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
                return [arr[left]]

            mid = (left + right) // 2

            left_half = merge_sort(left, mid)
            right_half = merge_sort(mid + 1, right)
            count(left_half, right_half)

            return merge(left_half, right_half)

        cost = 0
        merge_sort(0, len(arr) - 1)

        return cost


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    arr = [[num, 0] for i, num in enumerate(nums)]

    solution = Solution()
    solution.solve(arr)
    for num, cnt in arr:
        print(num, end=" ")
        
    print()

    # print(*nums)
