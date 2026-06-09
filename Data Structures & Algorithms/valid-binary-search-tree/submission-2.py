# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -10000, 10000)

    def dfs(self, node, lower, upper):
        if not node or (not node.left and not node.right):
            return True

        if not node.left:
            return node.right.val > node.val and self.dfs(node.right, node.val, upper)

        if not node.right:
            return node.left.val < node.val and self.dfs(node.left, lower, node.val)

        if node.left.val >= node.val or node.right.val <= node.val:
            return False
        else:
            return self.dfs(node.left, lower, node.val) and self.dfs(node.right, node.val, upper)

        