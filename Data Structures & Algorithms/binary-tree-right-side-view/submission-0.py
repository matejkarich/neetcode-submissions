# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal = []
        self.bfs([root])
        return self.traversal

    def bfs(self, q):
        if not q or len(q) == 0:
            return

        queue = []

        while len(q) > 1:
            node = q.pop(0)
            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        node = q.pop()
        if node:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            self.traversal.append(node.val)

        print(queue)    

        self.bfs(queue)

        