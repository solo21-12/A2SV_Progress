class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        indexs = {num: i for i, num in enumerate(nums)}

        def dfs(arr, left, right):
            if left >= right:
                return None

            maxx = max(arr[left:right])
            node = TreeNode(maxx)

            i = indexs[maxx]

            node.left = dfs(arr, left, i)
            node.right = dfs(arr, i + 1, right)

            return node

        return dfs(nums, 0, len(nums))
