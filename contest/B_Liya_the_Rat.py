s = input()


prefix = [0] * (len(s))

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        prefix[i] = 1

for i in range(1,len(prefix)):
    prefix[i] += prefix[i-1]



m = int(input())

for _ in range(m):
    start,end = map(int, input().split())
    if start - 1 <= 0:
        print(prefix[end-2])
    else:
        print(prefix[end-2] - prefix[start - 2])


