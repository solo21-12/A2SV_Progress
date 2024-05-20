t = int(input())


def solution(c):

    c.sort()
    if c[0] != 1:
        return False
    prefixSum = 1

    for i in range(1, len(c)):

        if prefixSum < c[i]:
            return False

        prefixSum += c[i]
    return True


for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))

    if solution(c):
        print("YES")
    else:
        print("NO")
