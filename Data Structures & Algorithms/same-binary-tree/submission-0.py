# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        leftTree, rightTree = [], []
        self.inOrder(p, leftTree)
        self.inOrder(q, rightTree)
        print(leftTree)
        print(rightTree)
        return leftTree == rightTree

    def inOrder(self, root, traversal):
        if not root:
            return

        self.inOrder(root.left, traversal)
        traversal.append(root.val)
        self.inOrder(root.right, traversal)