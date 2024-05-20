class DisjontSet:

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
