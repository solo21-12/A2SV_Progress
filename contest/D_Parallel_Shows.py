from typing import List


t = int(input())

shows = []

for _ in range(t):
    a, b = map(int, input().split())
    shows.append([a, b])


def solve(shows: List):
    shows.sort(key= lambda x: (x[0], x[1]))

    tv1, tv2 = [], []
    tv1.append(shows[0])

    for start, end in shows[1:]:
        lastTv1End = tv1[-1][1]
        if start > lastTv1End:
            tv1.append([start, end])
        elif not tv2:
            tv2.append([start, end])
        elif tv2:
            lastTv2End = tv2[-1][1]
            if start > lastTv2End:
                tv2.append([start, end])

    return len(shows) == (len(tv1) + len(tv2))


if solve(shows):
    print('YES')
else:
    print('NO')
