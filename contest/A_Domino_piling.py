def findKthNumber(m: int, n: int, k: int) -> int:

    def check(num):
        count = 0
        for i in range(1, m + 1):
            count += min(num // i, n)


        return count >= (m * n) - (k - 1)

    low, high = 1, (m * n) + 1
    while low < high:
        mid = (low + high) // 2

        if check(mid):
            high = mid
        else:
            low = mid + 1

    return low


m, n, k = map(int, input().split())
print(findKthNumber(m, n, k))
