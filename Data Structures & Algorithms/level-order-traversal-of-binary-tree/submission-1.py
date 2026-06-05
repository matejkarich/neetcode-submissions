# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traversal = []
        queue = [root]
        self.bfs(queue)
        return self.traversal

    def bfs(self, queue):
        level = []
        nextQueue = []
        if len(queue) == 0:
            return
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                level.append(node.val)
                nextQueue.append(node.left)
                nextQueue.append(node.right)
        if len(level) > 0:
            self.traversal.append(level)
        return self.bfs(nextQueue)
