from leetcode.p0872.TreeNode import TreeNode


class Solution:
    @staticmethod
    def _dfs(root):
        if not root.left and not root.right:
            yield root.val
        if root.left:
            yield from Solution._dfs(root.left)
        if root.right:
            yield from Solution._dfs(root.right)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        x, y = list(Solution._dfs(root1)), list(Solution._dfs(root2))
        if len(x) != len(y):
            return False
        for i, v in enumerate(x):
            if v != y[i]:
                return False
        return True
