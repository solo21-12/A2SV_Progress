word = input()


def solve(word):
    stack = []

    for ch in word:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)


print(solve(word))
