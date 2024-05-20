n, k = map(int, input().split())
nums = list(map(int, input().split()))

suffix = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    suffix[i] += (nums[i] + suffix[i + 1])

suffix.pop()
result = suffix[0]

suffix = sorted(suffix[1:], reverse=True)
for num in suffix[:k - 1]:
    result += num

print(result)
