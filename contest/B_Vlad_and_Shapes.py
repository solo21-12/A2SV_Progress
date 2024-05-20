t = int(input())


def solver(arr):
    count = 0
    for one in arr:
        if count == 0:
            count = max(count, one)
        elif one == count:
            return "SQUARE"

    return "TRIANGLE"


for _ in range(t):
    n = int(input())
    arr = []

    for _ in range(n):
        nums = input()
        count = 0
        arr.append(nums.count('1'))

    print(solver(arr))
