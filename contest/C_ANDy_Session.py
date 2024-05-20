
def solve(num, k):
    ans = 0

    for i in range(30, -1, -1):
        count = 0
        all_one = True

        for num in nums:
            if num & (1 << i) == 0:
                count += 1
                all_one = False

        if count <= k:
            ans |= (1 << i)
            k -= count
        elif all_one:
            ans |= (1 << i)

    return ans


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    print(solve(nums, k))
