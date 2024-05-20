t = int(input())

def solve(n, k):
    op = n // k
    ans = []
    for i in range(k):
        ans.extend([chr(97 + i)] * op)
    
    if n % k:
        ans.extend([chr(97 + i) for i in range(n % k)])
        
    return ''.join(ans)
        
    

for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))