t = int(input())
def solve(nums):
    prefix = [nums[0]]
    
    cur = nums[0]
    
    for num in nums[1:]:
        cur &= num
        prefix.append(cur)
        
    print(prefix)


for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        
        
    solve(nums)