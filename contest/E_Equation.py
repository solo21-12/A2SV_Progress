import math
c = float(input())

low, high = -1, c / 2

for _ in range(100):
    mid = (low + high) / 2
    r = pow(mid, 2) + math.sqrt(mid)
    
    if r <= c:
        low = mid
    else:
        high = mid


print(low)

    