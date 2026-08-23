class TrieNode:

    def __init__(self):
        self.children = [None] * 27
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        self.helpAddWord(word, self.root) 

    def helpAddWord(self, word, curr):
        if word == "":
            curr.isEndOfWord = True
            return
        i = ord(word[0]) - ord('a')
        if not curr.children[i]:
            curr.children[i] = TrieNode()
        if not curr.children[26]:
            curr.children[26] = TrieNode()
        dot = curr.children[26]
        curr = curr.children[i]
        self.helpAddWord(word[1:], curr)
        self.helpAddWord(word[1:], dot)

    
    def search(self, word: str) -> bool:
        currentNode = self.root
        for c in word:
            if c == '.':
                indexInChildren = 26
            else:
                indexInChildren = ord(c) - ord('a')

            node = currentNode.children[indexInChildren]
            if not node:
                return False
            currentNode = node

        return currentNode.isEndOfWord
        
