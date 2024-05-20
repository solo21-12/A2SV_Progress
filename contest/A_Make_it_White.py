t = int(input())

def solver():
    n = int(input())

    s = input()

    left , right = 0, n - 1
    
    while left < n and s[left] != 'B':
        left += 1

    while right and s[right] != "B":
        right -= 1


    return right - left + 1


for _ in range(t):
    print(solver())
    
