from collections import defaultdict
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict
import threading


setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

n = int(stdin.readline())

adj = defaultdict(list)

for _ in range(n - 1):
    a, b, c = map(int, stdin.readline().split())

    adj[a].append((b, c))
    adj[b].append((a, c))

vis = set()
result_stack = []


def main():
    def dfs(current, dist):
        vis.add(current)

        for neigbour, new_dist in adj[current]:
            if neigbour not in vis:
                dfs(neigbour, dist + new_dist)

        result_stack.append((current, dist))

    dfs(0, 0)
    ans = 0

    for node, dist in result_stack:
        ans = max(ans, dist)

    print(ans)


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
