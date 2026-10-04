"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}
        
        def dfs(node):
            if not node:
                return None
            if node.val in nodeMap:
                return nodeMap[node.val]

            nodeMap[node.val] = Node(node.val)
            neighbors = []
            for n in node.neighbors:
               res = dfs(n)
               if res:
                neighbors.append(res)
            nodeMap[node.val].neighbors = neighbors
            return nodeMap[node.val]

        res = dfs(node)  
        print(nodeMap)
        return res
        