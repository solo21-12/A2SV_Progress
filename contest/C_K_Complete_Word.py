t = int(input())


def solve(word, k):

    nums = [[0 for _ in range(26)] for _ in range(k)]
    cur = 0

    for i in range(k):
        for j in range(i, len(word), k):
            idx = ord(word[j]) - ord('a')
            nums[i][idx] += 1

    for num in nums:
        maxx, cur_sum = 0, 0

        for i in num:
            maxx = max(i, maxx)
            cur_sum += i

        cur += (cur_sum - maxx)

    # print(nums)
    print(cur)


for _ in range(t):

    a, k = map(int, input().split())

    word = input()
    solve(word, k)
