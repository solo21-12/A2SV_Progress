class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()

        
        def find_no_sub_sequence(num, low, high):

            cnt = 0
            i = low
            while low < high:
                mid = low + (high - low) // 2

                if nums[mid] + num <= target:
                    low = mid + 1
                else:
                    high = mid

            cnt += pow(2, low - i - 1, MOD)
    
            return cnt

        res = 0
        for i, num in enumerate(nums):
            if num + num <= target:
                res += find_no_sub_sequence(num, i , len(nums))

        return res % MOD
        