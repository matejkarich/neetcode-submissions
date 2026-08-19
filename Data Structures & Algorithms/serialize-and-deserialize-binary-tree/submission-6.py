# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        serializedList = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node:
                serializedList.append("_")
            else:
                serializedList.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        print(",".join(serializedList))
        return ",".join(serializedList)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        components = data.split(",")
        if not components:
            return None
        index = 0
        root = TreeNode(components[index], None, None)
        queue = [root]
        while queue and index < len(components)-2:
            node = queue.pop(0)
            if node:
                if components[index+1] == '_':
                    left = None
                else:
                    left = TreeNode(components[index+1], None, None)
                    queue.append(left)

                if components[index+2] == '_':
                    right = None
                else:
                    right = TreeNode(components[index+2], None, None)
                    queue.append(right)
                node.left = left
                node.right = right
            index += 2
        return root
