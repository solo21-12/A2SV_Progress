class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = str(int("".join(map(str, digits))) + 1)
        ans = [int(ch) for ch in val]

        return ans
