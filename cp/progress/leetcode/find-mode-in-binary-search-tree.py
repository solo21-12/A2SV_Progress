# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:


        def dfs(root):
            if not root:
                return

            count.append(root.val)
            dfs(root.left)
            dfs(root.right)

        count = []
        dfs(root)

        temp = Counter(count).most_common()
        ans = []
        for key, value in temp:
            if value == temp[0][1]:
                ans.append(key)

        return ans
