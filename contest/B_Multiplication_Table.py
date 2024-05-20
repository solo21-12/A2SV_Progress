def findKthNumber(m: int, k: int) -> int:

    def check(num):
        count = 0
        for i in range(1, m + 1):
            count += min(num // i, m)

        return count >= k

    low, high = 1, (m * m) + 1
    while low < high:
        mid = (low + high) // 2

        if check(mid):
            high = mid
        else:
            low = mid + 1

    return low


m, n = map(int, input().split())
print(findKthNumber(m, n))
