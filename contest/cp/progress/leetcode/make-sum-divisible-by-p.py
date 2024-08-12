class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totalRem = sum(nums) % p
        n = len(nums)

        if not totalRem:
            return 0

        answer = n
        prefixSum = 0
        hashmap = {0:-1}

        for i,num in enumerate(nums):

            prefixSum += num
            curRem = prefixSum % p
            key = (curRem - totalRem) % p

            if key in hashmap:
                answer = min(answer, i-hashmap[key])

            hashmap[curRem] = i

        return answer if answer < n else -1


        

        
        

        




        