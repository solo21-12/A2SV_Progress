from collections import Counter
import decimal
 
 
def solve(a, b, n):
    nums = []
    zeros = 0
    for i, j in zip(a, b):
        if i == 0 and j == 0:
            zeros += 1
        elif i != 0:
            nums.append(decimal.Decimal(j) / decimal.Decimal(i))
        else:
            continue
 
    counts = Counter(nums).most_common()
    return counts[0][1] + zeros if counts else zeros
 
 
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = solve(a, b, n)
print(ans)

