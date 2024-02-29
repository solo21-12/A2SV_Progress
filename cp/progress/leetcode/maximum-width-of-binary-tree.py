# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q = deque([root])
        maxCount = 0
        root.val = 1

        while q:
            N = len(q)
            count = []

            for _ in range(N):
                top = q.popleft()

                if top:
                    if top.left:
                        top.left.val = top.val * 2
                        q.append(top.left)
                    if top.right:
                        top.right.val = (top.val * 2) + 1
                        q.append(top.right)

                    count.append(top.val)

            maxCount = max(maxCount, count[-1] - count[0] + 1)

        return maxCount
