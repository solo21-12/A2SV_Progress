import math
def solve(nums, n):
    count = 0
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            x = math.ceil(nums[i - 1] / nums[i])

            res = math.ceil(math.log2(x))
            
            count += res

            nums[i] *= pow(2, res)

    return count


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    ans = solve(nums, n)
    print(ans)
