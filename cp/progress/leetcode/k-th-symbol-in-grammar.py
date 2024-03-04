class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def backtrack(N, k):
            if N == 1:
                return 0

            total_elements = 2 ** (N - 1)
            half_elements = total_elements // 2

            if k > half_elements:
                return 1 - backtrack(N, k - half_elements)

            return backtrack(N - 1, k)

        
        return backtrack(n, k)

        