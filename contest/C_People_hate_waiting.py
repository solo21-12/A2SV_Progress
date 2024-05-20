n = int(input())

queue = list(map(int, input().split()))
queue.sort()

count,prefix,l = 0,0,0

while l < len(queue):
    if queue[l] >= prefix:
        count += 1
        prefix += queue[l]
        l += 1
    else:
        l += 1

print(count)
