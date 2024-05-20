
from sys import stdin, stdout, setrecursionlimit
import threading
from collections import defaultdict


class DSURank:
    def __init__(self, n) -> None:
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))

    def find_parent(self, child):
        if self.parent[child] != child:
            self.parent[child] = self.find_parent(self.parent[child])

        return self.parent[child]

    def union(self, child_one, child_two):
        parent_one, parent_two = self.find_parent(
            child_one), self.find_parent(child_two)

        if parent_one == parent_two:
            return

        rank_one, rank_two = self.rank[parent_one], self.rank[parent_two]

        if rank_one > rank_two:
            self.parent[parent_two] = parent_one
        elif rank_two > rank_one:
            self.parent[parent_one] = parent_two
        else:
            self.parent[parent_two] = parent_one
            self.rank[parent_one] += 1

    def connected(self, child_one, child_two) -> bool:
        return self.find_parent(child_one) == self.find_parent(child_two)


class DSUSize:
    def __init__(self, n) -> None:
        self.size = [0] * (n + 1)
        self.parent = list(range(n + 1))

    def find_parent(self, child) -> int:
        if self.parent[child] != child:
            self.parent[child] = self.find_parent(self.parent[child])

        return self.parent[child]

    def union(self, child_one, child_two) -> None:
        parent_one, parent_two = self.find_parent(
            child_one), self.find_parent(child_two)

        if parent_one == parent_two:
            return

        size_one, size_two = self.size[parent_one], self.size[parent_two]

        if size_one > size_two:
            self.parent[parent_two] = parent_one
            self.size[parent_one] += size_two
        elif size_two > size_one:
            self.parent[parent_one] = parent_two
            self.size[parent_two] += size_one
        else:
            self.parent[parent_two] = parent_one
            self.size[parent_one] += size_two

        def connected(self, child_one, child_two) -> bool:
            return self.find_parent(child_one) == self.find_parent(child_two)


setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)


def main():
    # Enter your code here
    pass


main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()


