from typing import Counter


def solve(word):
    count = Counter(word)

    return len(word) - 1 if len(count) > 1 else -1


t = int(input())

for _ in range(t):
    word = input()

    print(solve(word))
