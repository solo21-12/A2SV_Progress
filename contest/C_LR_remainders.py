t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    nums = list(map(int,input().split()))

    commands = input()


    totalProduct = 1
    for num in nums:
        totalProduct *= num

    l = 0
    r = len(nums) - 1
    
    print(totalProduct % m, end=" ")
    for i in range(len(commands) - 1):
        command = commands[i]
        if command == 'L':
            totalProduct //= nums[l]
            l += 1
        else:
            totalProduct //= nums[r]
            r -= 1
        print(totalProduct % m, end=" ")

    print()

