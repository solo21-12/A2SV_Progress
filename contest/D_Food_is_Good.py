t = int(input())

def get_ans(tastiness, simon):
    currSum, maxSum = 0, float('-inf')

    for i in range(len(tastiness)):
        currSum += tastiness[i]

        maxSum = max(maxSum, currSum)

        if currSum < 0:
            currSum = 0

    return simon > maxSum


for _ in range(t):
    n = int(input())

    tastiness = list(map(int, input().split()))
    simon = sum(tastiness)


    if get_ans(tastiness[:n-1], simon) and get_ans(tastiness[1:n], simon):
        print("YES")
    else:
        print("NO")
