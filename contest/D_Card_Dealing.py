def solve(n):
    her = 0
    bob = 0

    t = 1
    c = 1

    while c < n:
        n -= c
        if t > 0:
            her += c
            c += 4

        else:
            bob += c
            c += 4

        t *= -1

    if n:
        if t > 0:
            her += n
        else:
            bob += n

    print(her, bob)


for _ in range(int(input())):
    n = int(input())

    solve(n)
