import enum
import threading
from collections import defaultdict
from sys import stdin, stdout, setrecursionlimit


class DSURank:
    def __init__(self, n) -> None:
        self.node_ranks = [0] * (n + 1)
        self.node_parents = list(range(n + 1))

    def find_parent(self, node_index):
        if self.node_parents[node_index] != node_index:
            self.node_parents[node_index] = self.find_parent(
                self.node_parents[node_index])
        return self.node_parents[node_index]

    def union(self, index_one, index_two):
        parent_index_one, parent_index_two = self.find_parent(
            index_one), self.find_parent(index_two)

        if parent_index_one == parent_index_two:
            return

        rank_parent_one, rank_parent_two = self.node_ranks[
            parent_index_one], self.node_ranks[parent_index_two]

        if rank_parent_one > rank_parent_two:
            self.node_parents[parent_index_two] = parent_index_one
        elif rank_parent_two > rank_parent_one:
            self.node_parents[parent_index_one] = parent_index_two
        else:
            self.node_parents[parent_index_two] = parent_index_one
            self.node_ranks[parent_index_one] += 1

    def connected(self, index_one, index_two) -> bool:
        return self.find_parent(index_one) == self.find_parent(index_two)


setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    dsu = DSURank(n)
    for i, num in enumerate(nums):
        dsu.union(i + 1, num)

    count = defaultdict(int)
    for i, num in enumerate(dsu.node_parents):
        if i > 0:
            parent = dsu.find_parent(num)
            count[parent] += 1

    print(len(count))


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
