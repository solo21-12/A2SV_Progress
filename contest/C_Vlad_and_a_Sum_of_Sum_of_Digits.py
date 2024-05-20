
prefixSum = [0] * (2  * (10 ** 5) + 1)

for i in range(1,2  * (10 ** 5) + 1 ):
    prefixSum[i] = prefixSum[i-1] + sum(map(int, str(i)))


t = int(input())

for _ in range(t):
    num = int(input())
    print(prefixSum[num])
    
