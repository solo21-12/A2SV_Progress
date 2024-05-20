

def solve(a, b, x):
    minA = min(a)
    maxB = max(b)

    if minA + maxB > x:
        return False

    a.sort()
    b.sort(reverse=True)
    for i in range(len(a)):
        if a[i] + b[i] > x:
            return False
    return True


t = int(input())

for i in range(t):
    if i >= 1:
        x = input()
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if solve(a, b, x):
        print('Yes')
    else:
        print('No')
