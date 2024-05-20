t = int(input())


def solution(waterContainers, n):

    target = sum(waterContainers) // n

    for i in range(n - 1):
        if waterContainers[i] < target:
            return False
        
        waterContainers[i + 1] += waterContainers[i] - target
        waterContainers[i] = target

    return True


for _ in range(t):
    n = int(input())

    waterContainers = list(map(int, input().split()))

    if solution(waterContainers, n):
        print("YES")
    else:
        print("NO")
