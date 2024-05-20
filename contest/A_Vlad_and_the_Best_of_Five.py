t = int(input())

for _ in range(t):
    s = input()
    A = s.count('A')
    B =  5 - A

    if A > B:
        print("A")
    else:
        print('B')