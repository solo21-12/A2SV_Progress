t = int(input())

def solve(word):
    return word + word[::-1]

for _ in range(t):
    word = input()
    print(solve(word))
    