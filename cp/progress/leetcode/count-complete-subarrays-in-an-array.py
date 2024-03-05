class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(set(nums))
        count = 0
        l = 0
        window = defaultdict(int)

        for r in range(len(nums)):
            window[nums[r]] += 1

            while len(window) == N:
                count += len(nums) - r

                window[nums[l]] -= 1

                if window[nums[l]] == 0:
                    window.pop(nums[l])

                l += 1

        return count
