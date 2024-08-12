class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        numsLeft = 0
        numsRight = nums.count(1)
        count = defaultdict(list)
        count[numsRight].append(0)

        for i,num in enumerate(nums):
            if num:
                numsRight -= 1
            else:
                numsLeft += 1

            count[numsLeft + numsRight].append(i+1)

        maxx = max(count.keys())

        return count[maxx]


        


        