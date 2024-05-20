from collections import deque
import re


n = int(input())

ax, ay = map(int, input().split())
bx, by = map(int, input().split())

board = []

for _ in range(n):
    row = list(input())

    board.append(row)

row, col = len(board), len(board[0])


def inbound(new_row, new_col):
    return 0 <= new_row < n and 0 <= new_col < n


vis = set()
q = deque()
d = col
direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def add_cells(idx, x, y, count):
    dx, dy = direction[idx]

    for r in range(1,d + 1):
        new_row, new_col = x + (dx * r), y + (dy * r)

        if inbound(new_row, new_col) and (new_row, new_col) not in vis:
            if board[new_row][new_col] == '#':
                break
            else:
                q.append((new_row, new_col, count + 1))
                # vis.add((new_row, new_col))
        

q.append((ax, ay, 0))

    
def bfs():
    
    while q:
        
        x, y, count = q.popleft()
        vis.add((x, y))
        
        if (x, y) == (bx, by):
            return count

        for i in range(4):
            add_cells(i, x, y, count)
            
    return -1

print(bfs())
