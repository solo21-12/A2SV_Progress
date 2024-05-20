s = input()


def solve(s):
    stack = []
    ans = []

    suffix = [s[-1]] * len(s)

    for i in range(len(s) - 2, -1, -1):
        suffix[i] = min(suffix[i + 1], s[i])
    # print(suffix)
    for i in range(len(s)):
        if s[i] <= suffix[i]:
            while stack and stack[-1] < s[i]:
                ans.append(stack.pop())
            ans.append(s[i])
        else:
            while stack and stack[-1] < suffix[i]:
                ans.append(stack.pop())
            stack.append(s[i])

    while stack:
        ans.append(stack.pop())

    return "".join(ans)


print(solve(s))
