import math
def possibele(demand, time, num, target):
    cnt = 0
    
    for i, d in enumerate(demand):
        r = math.ceil(d / num)
        cnt += (r * time[i])
    
    # print(cnt, target)
    return cnt <= target


def solve(demand, time, k):
    low, high = 1, max(demand)
    
    while low < high:
        mid = (low + high) // 2
        if possibele(demand, time, mid, k):
            high = mid
        else:
            low = mid + 1
    
    if possibele(demand, time, low, k):
        print(low)
    else:
        print(-1)   
            
    

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    demand = list(map(int, input().split()))
    time = list(map(int, input().split()))
    

    solve(demand, time, k)
    
    