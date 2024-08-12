class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def generate( i, arr):
            N = len(nums)
            if i >= N:
                ans.append(arr[::])
                return

            # This is the case when we select the current index element
            arr.append(nums[i])
            generate(i + 1, arr)

            # This is the case when we don't select the current index element
            arr.remove(nums[i])
            generate(i + 1, arr)

        generate(0, [])

        return ans
