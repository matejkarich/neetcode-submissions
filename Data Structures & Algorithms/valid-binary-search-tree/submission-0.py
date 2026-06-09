# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        elif not root.left:
            return root.right.val > root.val
        elif not root.right:
            return root.left.val < root.val

        return root.left.val < root.val and root.right.val > root.val and self.isValidBST(root.left) and self.isValidBST(root.right)

        