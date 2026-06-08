# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, node, largestInPath):
        if not node:
            return 0

        if node.val >= largestInPath:
            return 1 + self.dfs(node.left, node.val) + self.dfs(node.right, node.val)

        else:
            return self.dfs(node.left, largestInPath) + self.dfs(node.right, largestInPath)

        