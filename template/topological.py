
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
import threading



setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def main():
    # Enter your code here
    pass


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()


n = int(input())
graph = defaultdict(list)
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(i + 1, len(row)):
        graph[i].append((j, row[j]))
        graph[j].append((i, row[i]))


t = int(input())  # number of test cases
for _ in range(t):
    # number of nodes and edges
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for j in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)


t = int(input())  # number of test cases
for _ in range(t):
    # number of nodes and edges
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for j in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)


import sys
input = sys.stdin.readline()




