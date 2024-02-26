# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        h = defaultdict(list)
        ans = []

        def inOrder(root, row, col):
            nonlocal h
            if not root:
                return

            inOrder(root.left, row + 1, col - 1)
            h[col].append([root.val, row])
            inOrder(root.right, row + 1, col + 1)

        inOrder(root, 0, 0)

        for key in sorted(list(h.keys())):
            h[key] = sorted(h[key], key=lambda x: (x[1], x[0]))
            ans.append([num[0] for num in h[key]])

        return ans
