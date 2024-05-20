    
    
def counter(council, nums, k):
    evens = 0
    rem = 0
    for n in nums:
        evens += (n // k)
        rem += (n % k)
        
    return evens + (rem // k) >= council
    

k = int(input())
n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))
    
    
low, high  = 0, 1e10

while high > low + 1:
    mid = (low + high) // 2
    
    if counter(mid, nums, k):
        low = mid 
    else:
        high = mid
        
        
print(int(low))
    
