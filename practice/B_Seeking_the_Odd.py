
def solve(n):
    while n % 2 == 0:
        n //= 2
    
    return n > 1


t = int(input())


for _ in range(t):
    n = int(input())

    if solve(n):
        print("YES")
    else:
        print("NO")
