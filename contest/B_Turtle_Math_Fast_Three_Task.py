t = int(input())


for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    totalSum = sum(nums)

    
    if totalSum % 3:

        nums.sort()
        count = 0
        prevMultiple = ((totalSum // 3)) * 3
        rem = totalSum - prevMultiple
        print(prevMultiple,":")
        
        for num in nums:
            if num < rem:
                rem -= num
                count += 1
                
       
        count += rem

        
        nextMultiple = ((totalSum // 3) + 1) * 3
        diff = nextMultiple - totalSum
        count2 = 0
        for num in nums[::-1]:
            if (totalSum - num) + (num + diff) == nextMultiple:
                count2 = 1
                
        print(min(count2, count))
        
    else:
        print('0')
        

