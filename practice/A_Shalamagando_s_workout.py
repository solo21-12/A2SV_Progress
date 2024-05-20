from collections import defaultdict


n = int(input())
nums = list(map(int, input().split()))


def solve(nums):

    exericise = defaultdict(int)
    ans = {
        0: 'chest',
        1: 'biceps',
        2: 'back'
    }

    for i, num in enumerate(nums):
        idx = i % 3
        exericise[idx] += num

    max_occures = 0

    for key, val in exericise.items():
        if val > exericise[max_occures]:
            max_occures = key

    return ans[max_occures]


print(solve(nums))
