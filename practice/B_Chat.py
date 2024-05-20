from collections import defaultdict
from email.policy import default
from heapq import heappush, heappop, heappushpop

n, k, q = map(int, input().split())
nums = list(map(int, input().split()))

online_copy = defaultdict(int)
online = []

for _ in range(q):
    types, idx = input().split()
    idx = int(idx)

    if types == '1':
        if len(online) < k:
            heappush(online, (nums[idx - 1], idx))
            online_copy[idx] += 1
        else:
            minn, new_id = online[0]
            if minn >= nums[idx - 1]:
                continue
            else:
                heappushpop(online, (nums[idx - 1], idx))
                online_copy.pop(new_id)
                online_copy[idx] += 1
    else:
        if online_copy[idx]:
            print('YES')
        else:
            print('NO')
