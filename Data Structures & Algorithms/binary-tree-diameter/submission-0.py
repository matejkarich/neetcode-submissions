# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0
        d = self.dfs(node.left) + self.dfs(node.right)
        self.res = max(self.res, d)
        return 1 + max(self.dfs(node.left), self.dfs(node.right))