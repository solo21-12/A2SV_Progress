t = int(input())


def solve(nums, x):
    nums.sort()
    ans  = 0
    temp = 0

    for i in range(len(nums) - 1,-1,-1):
        if nums[i] >= x:
            ans += 1
        else:
            if temp and (temp +1) * nums[i] >= x :
                pass
    

   

for _ in range(t):
    n, x = map(int, input().split())

    nums = list(map(int, input().split()))

    print(solve(nums, x))
