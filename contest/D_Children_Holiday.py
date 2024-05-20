m, n = map(int, input().split())

arr = []
for _ in range(n):
    t, z, y = map(int, input().split())
    arr.append([t, z, y])


def isBallonPossible(t, z, y, ballons, time):
    batchTime = (z * t) + y
    batches = ballons // z

    ok = (ballons % z == 0)
    currTime = 0

    if ok:
        batches -= 1
        currTime = (batchTime * batches) + (z * t)
    else:
        currTime = (batchTime * batches) + ((ballons % z) * t)

    return currTime <= time


def isPossible(time):
    totalBallons = 0

    for i, (t, z, y) in enumerate(arr):
        l, h = 0, 1e9

        while h > l + 1:
            ballons = (l + h) // 2

            if isBallonPossible(t, z, y, ballons, time):
                l = ballons
            else:
                h = ballons
        totalBallons += l

    return totalBallons >= m

def countMaxBallons(t, z, y, maxTime):
    batchTIme = (z*t) + y
    batchCount = (maxTime// batchTIme)
    remTime = (maxTime % batchTIme)
    totalBallons = batchCount * z
    if remTime != 0:
        if remTime // t >= z:
            totalBallons +=z
        else:
            totalBallons += remTime // t
    return totalBallons
    


def solve():
    minTime, maxTime = -1, 1e9

    while maxTime > minTime + 1:
        midTime = (minTime + maxTime) // 2

        if isPossible(midTime):
            maxTime = midTime
        else:
            minTime = midTime

    return int(maxTime)

print(solve())
