def solve(nums, n):
    prefixSum = nums[0] + 1

    for i, num in enumerate(nums[1:]):
        while num < prefixSum:
            num += num

        print(prefixSum, num, i)

        nums[i+1] = num

        prefixSum += num

    return nums[-1]
    


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    print(solve(nums, n))


