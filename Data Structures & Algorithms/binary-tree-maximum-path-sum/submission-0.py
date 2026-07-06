# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.currentMax = float("-inf")
        self.traverse(root)
        return self.currentMax

    def traverse(self, root):
        if not root:
            return 0

        left = self.traverse(root.left)
        right = self.traverse(root.right)
        path = max(self.currentMax, left + root.val, right+root.val, root.val)
        terminalPath = left + right + root.val
        if path >= terminalPath:
            self.currentMax = path
            return max(left + root.val, right + root.val, root.val)
        else:
            self.currentMax = terminalPath
            return 0