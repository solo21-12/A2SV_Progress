t = int(input())

def solve(n):
    nums = [0] * (n)
    nums[0] = n
    for i in range(1, n):
        nums[i] = i
        
    return nums

for _ in range(t):
    n = int(input())
    
    print(*solve(n))