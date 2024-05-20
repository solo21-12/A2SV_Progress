def solve(pin):
    # Your implementation goes here

    cursor = 1
    res = len(pin)
    for num in pin:
        if num == '0':
            res += 10 - cursor
            cursor = 10
        else:
            res += abs(int(num) - cursor)
            cursor = int(num)
    return res


t = int(input())

for _ in range(t):
    pin = (input())

    ans = solve(pin)
    print(ans)
