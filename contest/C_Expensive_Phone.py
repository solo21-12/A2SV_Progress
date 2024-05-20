t = int(input())


def solve(prices):
    nums = 0
    stack = []

    for i in range(len(prices)):

        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()
            nums += 1

        stack.append(i)

    return nums


for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    print(solve(prices))
