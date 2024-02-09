class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        points = [0] * (len(nums) + 1)
        ans = 0
        nums.sort()

        # calculating the prefix sum
        for start,end in requests:
            points[start] += 1
            points[end + 1] -= 1

        for i in range(1,len(points)):
            points[i] += points[i-1]

        points.pop()
        points.sort()
        
        # mapping the max occured points to the max requested index
        for i in range(len(points)):
            currSum = points[i] * nums[i]
            ans += currSum

        return ans % (10**9 + 7)


        