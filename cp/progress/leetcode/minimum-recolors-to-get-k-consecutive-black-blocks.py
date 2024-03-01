class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)
        ans = N

        l = 0
        whites = 0
        for r in range(N):
            if blocks[r] == 'W':
                whites += 1
                
            if r - l + 1 == k:
                ans = min(ans, whites)

                if blocks[l] == 'W':
                    whites -= 1

                l += 1

        return ans 

        