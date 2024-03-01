class Solution:
    def isValid(self, path):
        opened = 0
        for ch in path:
            if ch == ")":
                if not opened:
                    return False
                else:
                    opened -= 1
            else:
                opened += 1

        return opened == 0

    def generateParenthesis(self, n: int) -> List[str]:

        def generateAllCombinations(path, opened, closed):
            nonlocal ans
            if len(path) == (2 * n):
                ans.append(path)
                return

            if opened < closed:
                return

            if opened < n:
                generateAllCombinations(path + "(", opened + 1, closed)
            if closed < n:
                generateAllCombinations(path + ")", opened, closed + 1)

        ans = []
        generateAllCombinations("",0,0)

        return ans
