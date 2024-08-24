t = int(input())


def solve(word):
    res = []
    s = set(list("trygub"))
    c = [0 for _ in range(26)]
    b = 0
    for ch in word:
        if ch in s:
            c[ord(ch) - ord("a")] += 1
        else:
            res.append(ch)

    for ch in "bugyrt":
        if c[ord(ch) - ord("a")] > 0:
            res.extend(ch * c[ord(ch) - ord("a")])

    return "".join(res)


for _ in range(t):
    n = int(input())
    word = input()

    print(solve(word))
