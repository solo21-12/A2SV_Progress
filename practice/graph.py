from collections import defaultdict
import sys

# t = int(input())
# lists = defaultdict(list)
# for _ in range(t):
#     nums = input().split()
#     for node in nums[1:]:
        
#         nod, weight = map(int, node.split(','))
#         lists[nums[0]].append((nod, weight))
    
    
# print(lists)


# n = int(sys.stdin.readline())
n = int(input())
graphs = defaultdict(list)


# for i in range(n):
#     rows = list(map(int, input().split()))
    
#     for j, weight in enumerate(rows):
#         graphs[i].append((j, weight))
        
        
    
    
# t = int(input())
for _ in range(n):
    src, dest,weight = map(int, input().split())
    graphs[src].append((dest,weight))
    
    
print(graphs)
        
    