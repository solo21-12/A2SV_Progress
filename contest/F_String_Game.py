from collections import Counter


def possible(length, counter, p, nums):

    for i in range(length):
        counter[nums[i] - 1] = ''
    
    cnt = 0
    l, r =0, 0
    
    while l < len(counter) and r < len(p):
        if counter[l] == p[r]:
            cnt += 1
            r += 1
        
        l += 1
            
    return cnt == len(p)
    

t = input()
counter = list(t)
p = input()

nums = list(map(int, input().split()))

low, high = 0, len(t)


while high > low + 1:
    mid = (low + high) // 2

    if possible(mid, counter.copy(), p,  nums):
        low = mid
    else:
        high = mid

print(low)
