class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened, closed = 0, 0

        for ch in s:
            if ch == "(":
                opened += 1

            else:
                if opened:
                    opened -= 1
                else:
                    closed += 1

        return opened + closed
