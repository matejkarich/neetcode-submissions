# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.rootList = preorder
        return self.traverse(inorder)

    def traverse(self, vals):
        if not vals:
            return None

        root = self.rootList.pop(0)
        indexOfRoot = vals.index(root)
        leftVals = vals[:indexOfRoot]
        rightVals = vals[indexOfRoot+1:]
        
        leftNode = self.traverse(leftVals)
        rightNode = self.traverse(rightVals)
        return TreeNode(root, leftNode, rightNode)
        