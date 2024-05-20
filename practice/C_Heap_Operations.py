from heapq import heappop, heappush
n = int(input())

operations = []

for _ in range(n):
    ind = input()
    if len(ind.split()) == 2:
        opp, num = ind.split()
        operations.append((opp, num))
    else:
        operations.append((ind, 0))


def insert(num):
    result.append(f'insert {num}')
    heappush(heap, int(num))


heap = []
result = []
for opp, expected in operations:
    if opp == 'insert':
        insert(expected)

    elif opp == 'getMin':
        while heap and int(expected) > heap[0]:
            heappop(heap)
            result.append('removeMin')

        if not heap or heap[0] != int(expected):
            insert(expected)

        result.append(f'getMin {expected}')

    else:
        if not heap:
            insert(0)

        heappop(heap)
        result.append(f'{opp}')

print(len(result))
for opp in result:
    print(opp)
