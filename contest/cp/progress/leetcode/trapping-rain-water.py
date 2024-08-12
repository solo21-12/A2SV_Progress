class Solution:
    def trap(self, height: List[int]) -> int:
        # N = len(height)
        # prefix = [height[0]] * N
        # suffix = [height[-1]] * N

        # for i in range(1, N):
        #     prefix[i] = max(prefix[i - 1], height[i])

        # for i in range(N - 2, -1 ,-1):
        #     suffix[i] = max(suffix[i + 1], height[i])

        # result = 0

        # for i, num in enumerate(height):
        #     result += min(prefix[i], suffix[i]) - num

        # return result

        N = len(height)

        l, r = 0, N - 1
        leftMax, rightMax = 0, 0
        result = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] >= leftMax:
                    leftMax = height[l]
                else:
                    result += leftMax - height[l]
                l += 1
            else:
                if height[r] >= rightMax:
                    rightMax = height[r]
                else:
                    result += rightMax - height[r]

                r -= 1


        return result



        