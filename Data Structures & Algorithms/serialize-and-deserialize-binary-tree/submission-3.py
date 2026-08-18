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
        self.serializedTree = []
        self.queue = []

        return ",".join(self.bfs(root))#.rstrip("_")
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        dataList = data.split(",")
        rootNode = TreeNode(dataList[0], None, None)
        self.queue = [rootNode]
        self.deserializeBfs(dataList, 1)
        return rootNode

    def deserializeBfs(self, dataList, index):
        if not self.queue or index >= len(dataList):
            return
        parent = self.queue.pop(0)
        if dataList[index] == '_':
            leftChild = None
        else:
            leftChild = TreeNode(dataList[index], None, None)
            self.queue.append(leftChild)

        if dataList[index+1] == '_':
            rightChild = None
        else:
            rightChild = TreeNode(dataList[index+1], None, None)
            self.queue.append(rightChild)

        parent.left = leftChild
        parent.right = rightChild
        self.deserializeBfs(dataList, index+2)


    def bfs(self, node):
        if not node:
            self.serializedTree.append("_")
        else:        
            self.queue.append(node.left)
            self.queue.append(node.right)
            self.serializedTree.append(str(node.val))

        if not self.queue:
            return self.serializedTree
        self.bfs(self.queue.pop(0))
