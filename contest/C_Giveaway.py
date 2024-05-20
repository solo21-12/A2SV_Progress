def solve(y, x, prices):
    high = max(len(prices) - ( x - y), len(prices) - x)
    low = min(len(prices) - ( x - y), len(prices) - x)

    if low > 0:
        return prices[high - 1] - prices[low - 1]
    else:
        return prices[high - 1]

    

n, q = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()


for i in range(1, n):
    prices[i] += prices[i-1]

for _ in range(q):
    x, y = map(int, input().split())

    print(solve(y, x, prices))


