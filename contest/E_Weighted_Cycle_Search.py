from collections import deque


class DSURank:
    def __init__(self, n) -> None:
        self.node_ranks = [0] * (n + 1)
        self.node_parents = list(range(n + 1))
        self.node_weight = [float('inf')] * (n + 1)

    def find_parent(self, node_index):
        if self.node_parents[node_index] != node_index:
            self.node_parents[node_index] = self.find_parent(
                self.node_parents[node_index])
        return self.node_parents[node_index]

    def union(self, index_one, index_two, weight):
        parent_index_one, parent_index_two = self.find_parent(
            index_one), self.find_parent(index_two)

        if parent_index_one == parent_index_two:
            return

        rank_parent_one, rank_parent_two = self.node_ranks[
            parent_index_one], self.node_ranks[parent_index_two]

        if rank_parent_one > rank_parent_two:
            self.node_parents[parent_index_two] = parent_index_one
            self.node_weight[parent_index_one] = min(
                weight, self.node_weight[parent_index_one])

        elif rank_parent_two > rank_parent_one:
            self.node_parents[parent_index_one] = parent_index_two
            self.node_weight[parent_index_one] = min(
                weight, self.node_weight[parent_index_two])

        else:
            self.node_parents[parent_index_two] = parent_index_one
            self.node_ranks[parent_index_one] += 1
            self.node_weight[parent_index_one] = min(
                weight, self.node_weight[parent_index_one])



def is_cyclce(node, count):
    q = deque()

def solve(edges_list, n):
    dsu = DSURank(n)
    for a, b, w in edges_list:
        dsu.union(a, b, w)

    print(dsu.node_weight)


for _ in range(int(input())):
    n, m = map(int, input().split())

    edges_list = []

    for _ in range(m):
        a, b, w = map(int, input().split())
        edges_list.append((a, b, w))

    solve(edges_list, n)
