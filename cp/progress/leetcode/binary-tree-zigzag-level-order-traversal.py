# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        def levelOrder(root):
            if not root:
                return

            q = deque()
            q.append(root)
            flip = 1

            while q:
                N = len(q)

                temp = []
                for i in range(N):
                    node = q.popleft()
                    temp.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                ans.append(temp[::flip])
                flip *= -1

        levelOrder(root)

        

        return ans
