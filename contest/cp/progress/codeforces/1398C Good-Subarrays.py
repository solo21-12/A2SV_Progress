def solve(nums, n):
    s = 0
    res = 0
    prefix = {0: 1}
    for i, num in enumerate(nums):
        s += int(num)
        x = s - i - 1
        prefix[x] = prefix.get(x, 0) + 1

        res += prefix[x] - 1

    return res


t = int(input())

for _ in range(t):
    n = int(input())
    word = input()

    ans = solve(word, n)
    print(ans)
