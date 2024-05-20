from collections import deque


n, q = map(int, input().split())
nums = list(map(int, input().split()))

d = deque(nums)
result = []
for i in range(len(nums) - 1):
    a = d.popleft()
    b = d.popleft()

    result.append([a, b])
    d.appendleft(max(a, b))
    d.append(min(a, b))


def solve2(pos, n, d, maxx, result):

    if pos < n:
        return result[pos - 1]
    else:
        pos = pos % (n - 1)
        return [maxx, d[pos - 1]]


maxx = d.popleft()
for _ in range(q):
    pos = int(input())
    res = solve2(pos, n, d, maxx, result)
    print(*res)
