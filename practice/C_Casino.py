def find(num):
    for i in range(2, 4):

        while num % i == 0:
            num //= i

    return num


def solve(nums, n):
    cur = find(nums[0])

    for num in nums[1:]:
        if cur != find(num):
            return False

    return True


n = int(input())
nums = list(map(int, input().split()))

if solve(nums, n):
    print("Yes")
else:
    print("No")
