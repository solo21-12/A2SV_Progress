# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return

        q = deque([root])
        prev = 0
        even = 1

        while q:
            N = len(q)

            for i in range(N):
                top = q.popleft()

                if top:
                    if even == -1:
                        if (prev and top.val >= prev) or top.val % 2:
                            return False
                    else:
                        if (prev and top.val <= prev) or top.val % 2 == 0:
                            return False

                    prev = top.val
                    q.append(top.left)
                    q.append(top.right)

            prev = 0
            even *= -1

        return True
