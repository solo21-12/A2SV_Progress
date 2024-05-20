class Solution:
    def __init__(self) -> None:
        self.count = set()
        
    def partition(self, nums, pivot):
        N = len(nums)
        less, up, r = 0, N - 1, 0
        
        while r <= up:
            if nums[r] <= pivot:
                r += 1
                less += 1
            else:
                nums[r], nums[up] = nums[up], nums[r]
                up -= 1
                
        return less
                
    def qsort(self, nums):
        self.count.add(sum(nums))
        
        if len(nums) <= 1:
            return
        maxx = max(nums)
        minn = min(nums)
        
        
        if maxx == minn:
            return

        mid = (maxx + minn) // 2
        
        pi = self.partition(nums, mid)
        left_half = nums[:pi]
        right_half = nums[pi:]
                
        self.qsort(left_half)
        self.qsort(right_half)
        
    def solve(self,num):
        if num in self.count:
            return "Yes"

        return "No"
        
        

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())  
    nums = list(map(int, input().split()))
    
    for _ in range(q):
        si = int(input())     
        solution = Solution()
        solution.qsort(nums[:])
        print(solution.solve(si))
