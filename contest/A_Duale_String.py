t = int(input())


def solve(word):
    N = len(word)

    return word[:N//2] == word[N//2:]


for _ in range(t):
    word = input()
    if solve(word):
        print("YES")
    else:
        print("NO")
