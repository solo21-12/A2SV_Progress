import math


def solve(nums, n):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            gcd = math.gcd(nums[i], nums[j])
            cnt += gcd * (n - j - 1)
            
    return cnt


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        nums.sort()

        ans = solve(nums, n)
        print(ans)


if __name__ == "__main__":
    main()
