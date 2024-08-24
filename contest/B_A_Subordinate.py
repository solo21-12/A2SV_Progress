a, b = map(int, input().split())
k, m = map(int, input().split())

numsA = list(map(int, input().split()))
numsB = list(map(int, input().split()))


if numsA[k - 1] < numsB[-m]:
    print("YES")
else:
    print("NO")
