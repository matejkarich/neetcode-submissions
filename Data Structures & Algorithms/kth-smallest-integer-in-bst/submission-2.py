# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.smallest = None
        self.dfs(root, k)
        return self.smallest.val

    def dfs(self, node, k):
        if not node or self.smallest:
            return 0
        leftResult = self.dfs(node.left, k) + 1
        if leftResult == k:
            self.smallest = node
            return k + 1
        rightResult = self.dfs(node.right, k-leftResult) + leftResult
        return rightResult


        