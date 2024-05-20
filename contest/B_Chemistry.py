from collections import Counter


def solve(word, n, k):
    count = Counter(word)
    odd = 0
    for val in count.values():
        if val % 2:
            odd += 1
    minn = min(k, odd)
    odd -= minn
    k -= minn

    if odd > 1:
        return False

    return True


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    word = input()

    ans = solve(word, n, k)
    if ans:
        print("YES")
    else:
        print('NO')
