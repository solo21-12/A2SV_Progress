from functools import reduce


def solve(nums, n):
    product = reduce(lambda x, y: (x*y), nums)
    print(product)
    cnt = 0
    d = n
    if n % 2:
        d = n - 1
    
    while d > 0 and product % (2 ** n) != 0:
        cnt += 1
        product *= d
        d -= 2
    # print(cnt)
    # return cnt


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    ans = solve(nums, n)
    print(ans)
