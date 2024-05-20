from math import lcm


def find(word: str):
    new_word = word + word
    return new_word[1:].find(word)


def solve(word, nums, n):
    vis = set()
    result = 1
    for i in range(n):
        if i not in vis:
            path = ""
            while i not in vis:
                vis.add(i)
                path += word[i]
                i = nums[i] - 1

            idx = find(path)
            result = lcm(result, idx + 1)

    return result


t = int(input())

for _ in range(t):
    n = int(input())
    word = input()
    nums = list(map(int, input().split()))
    print(solve(word, nums, n))
