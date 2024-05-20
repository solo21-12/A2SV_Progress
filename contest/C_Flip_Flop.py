t = int(input())

def default(nums):
    prefix = [0]* len(nums)
    zeros = 1 if nums[-1] == 0 else 0
    for i in range(len(nums) - 2,-1,-1):
        num = nums[i]
        prefix[i] = zeros
        
        if num == 0:
            zeros += 1 
            
    ans =0
    
    for i in range(len(nums)):
        if nums[i] == 1:
            ans += prefix[i]
            
    return ans

def solve(nums):
    for i in range(len(nums)):
        if nums[i] != 1:
            nums[i] = 1
            break
        
        
    prefix = [0]* len(nums)
    zeros = 1 if nums[-1] == 0 else 0
    for i in range(len(nums) - 2,-1,-1):
        num = nums[i]
        prefix[i] = zeros
        
        if num == 0:
            zeros += 1 
            
    ans =0
    
    for i in range(len(nums)):
        if nums[i] == 1:
            ans += prefix[i]
            
    return ans
    
def solve2(nums):
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == 1:
            nums[i] = 0
            break
        
        
    prefix = [0]* len(nums)
    zeros = 1 if nums[-1] == 0 else 0
    for i in range(len(nums) - 2,-1,-1):
        num = nums[i]
        prefix[i] = zeros
        
        if num == 0:
            zeros += 1 
            
    ans =0
    
    for i in range(len(nums)):
        if nums[i] == 1:
            ans += prefix[i]
            
    return ans

for _ in range(t):
    n = int(input())
    
    nums = list(map(int, input().split()))
    
    nums2 = nums.copy()
    nums3 = nums.copy()
    ans = max(solve2(nums), solve(nums2), default(nums3))
    
    
    print(ans)
        
    
