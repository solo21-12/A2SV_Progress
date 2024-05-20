import math
from functools import reduce


def sum_of_factors(num):
    res = 1

    for d in range(2, math.ceil(math.sqrt(num))):
        cur_term = 1
        cur_sum = 1

        while num % d == 0:
            cur_term *= d
            cur_sum += cur_term
            num //= d

        res *= cur_sum

    return res


def find_gcd(num1, num2):

    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    return num1


def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1,)

    gcd, x1, y1 = gcd_extended(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)


def lcm_array(nums):
    res = nums[0]
    for num in nums[1:]:
        res = find_lcm(res, num)

    return res


def lcm_array2(nums):
    return reduce(lambda x, y: (math.lcm(x, y)), nums)


def gcd_array(nums):
    return reduce(lambda x, y: math.gcd(x, y), nums)

# nums = list(map(int, input().split()))
# print(gcd_array(nums))

# a, b = map(int, input().split())
# if find_gcd(a, b) == 1:
#     print(True)
# else:
#     print(False)


# def catalan(n):
#     if n <= 1:
#         return 1

#     res = 0
#     for i in range(n):
#         res += catalan(i) * catalan(n - i - 1)

#     return res


def catalan_DP(n):
    # O(N^2)
    catalan = [0] * (n + 1)
    catalan[0] = 1
    catalan[1] = 1
    for i in range(2, n + 1):

        for j in range(i):
            catalan[i] += (catalan[j] * catalan[i - j - 1])

    return catalan[n]


def b_c(n, r):
    if r > n - r:
        r = n - r

    ans = 1
    for i in range(r):
        ans = (ans * (n - i)) // (i + 1)

    return ans


def catalan_eff(n):
    return (b_c(2*n, n)) // (n + 1)


for i in range(int(input())):
    print(catalan_eff(i), end=" ")
