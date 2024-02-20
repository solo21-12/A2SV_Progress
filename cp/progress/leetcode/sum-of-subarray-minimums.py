class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        MOD = 10 ** 9 + 7
        result = 0

        for i, num in enumerate(arr):

            while stack and num < arr[stack[-1]]:
                index = stack.pop()
                left = index - stack[-1] if stack else index + 1
                right = i - index
                result += (arr[index] * left * right)

            stack.append(i)

        for i in range(len(stack)):
            index = stack[i]
            left = index - stack[i - 1] if i > 0 else index + 1
            right = len(arr) - index

            result += (arr[index] * left * right)

        return result % MOD