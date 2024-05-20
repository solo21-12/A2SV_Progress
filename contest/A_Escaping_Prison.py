def solve(nums, h):
    cnt = 0
    for w, t in nums:
        cnt += max(w, t)

    if cnt >= h:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    nums = []
    
    n, h = map(int, input().split())
    
    for _ in range(n):
        a, b = map(int, input().split())
        nums.append([a, b])

    solve(nums, h)
