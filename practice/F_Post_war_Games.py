def solve(n, k):
    if n == k:
        return 0
    sure = (n - (k + 1)) * 3 + (((k - 1 )// 2) * 3) + 1

    if (k - 1) % 2:
        sure += 1

    return sure


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    
        

    ans = solve(n, k)
    print(ans)
