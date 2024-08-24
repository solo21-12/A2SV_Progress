from typing import DefaultDict


t = int(input())


def solve(words, s):
    maps = DefaultDict(int)

    for i, ch in enumerate(words):
        maps[ch] = i

    count = 0

    for i in range(len(s) - 1):
        count += abs(maps[s[i]] - maps[s[i + 1]])

    return count


for _ in range(t):
    word = list(input())
    s = input()

    print(solve(word, s))
