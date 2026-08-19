class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

    def insert(self, word: str) -> None:
        if word == "":
            self.isLeaf = True
            return None
        letterLoc = ord(word[0]) - 97
        newTree = PrefixTree()
        self.children[letterLoc] = newTree
        newTree.insert(word[1:])

    def search(self, word: str) -> bool:
        if word == "":
            if self.isLeaf:
                return True
            return False
        letterLoc = ord(word[0]) - 97
        subTree = self.children[letterLoc]
        if not subTree:
            return False
        return subTree.search(word[1:])
        
    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True
        letterLoc = ord(prefix[0]) - 97
        subTree = self.children[letterLoc]
        if not subTree:
            return False
        return subTree.startsWith(prefix[1:])
        