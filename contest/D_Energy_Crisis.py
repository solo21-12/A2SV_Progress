n, k = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()


def solve(maxVal):
    dec = 0
    less = 0
    
    for num in nums:
        if num >= maxVal:
            dec += num - maxVal
        else:
            less += (maxVal - num)
            
    a = dec - (dec * k) / 100   

    return a >= less


low, high = 0, max(nums) + 1

for i in range(100):
    mid = (low + high) / 2
    
    if solve(mid):
        low = mid
    else:
        high = mid
        
print(f'{low}')
