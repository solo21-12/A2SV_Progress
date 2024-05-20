def solve(nums, n):
    for i in range(n):
        nums[i] = nums[i] % 10
        
    count = {0:1}
    c = 0
    
    for i in range(len(nums)):
        curSum = nums[i]
        c = 1
        
        for j in range(len(nums)):
            if j != i:
                curSum += nums[j]
                print(curSum)
                c += 1
                
                if c >= 3 and str(curSum)[-1] == '3':
                    return True
                
                diff = curSum - 3
                if c >=3 and count.get(diff, 0) > 0:
                    return True
                
                count[curSum] = count.get(curSum, 0) + 1
        count = {}
        
        
    return False
        
        
    
t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    ans = solve(nums, n)
    print(ans)