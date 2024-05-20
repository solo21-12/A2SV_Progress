
def solve(s):
    opened, closed = 0, 0

    for ch in s:
        if ch == "(":
            opened += 1
        else:
            if opened:
                opened -= 1
            else:
                closed += 1

    return len(s) - (opened + closed)

s = input()
print(solve(s))
