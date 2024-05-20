t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] *= - 1
            
    print(sum(nums))
