t = int(input())


def solve(word):

    opening = 1
    for i in range(1, len(word)):
        ch = word[i]
        if ch == '(' and word[i - 1] == ch:
            opening += 1

    return opening


for _ in range(t):
    n = int(input())
    word = input()
    print(solve(word))
