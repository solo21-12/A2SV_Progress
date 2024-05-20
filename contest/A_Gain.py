t = int(input())

for _ in range(t):
    n = int(input())
    strengths = list(map(int, input().split()))

    ans = []
    sortedStrength = sorted(strengths,reverse=True)

    highest = sortedStrength[0]
    secondHighes = sortedStrength[1]

    for strength in strengths:
        if strength == highest:
            ans.append(highest - secondHighes)
        else:
            ans.append(strength - highest)

    for i in range(len(ans)):
        print(ans[i],end=" ")

    print()
