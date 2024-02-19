class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            cur = temperatures[i]

            while stack and temperatures[stack[-1]] < cur:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans
