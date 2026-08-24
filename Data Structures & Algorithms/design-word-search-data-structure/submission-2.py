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
        curr = curr.children[i]
        self.helpAddWord(word[1:], curr)
    
    def search(self, word: str) -> bool:
        return self.helpSearch(word, self.root)

    def helpSearch(self, word, curr):
        if word == "":
            return curr.isEndOfWord
        if word[0] == '.':
            aggregate = False
            for child in curr.children:
                if child:
                    aggregate = aggregate or self.helpSearch(word[1:], child)
            return aggregate
        i = ord(word[0]) - ord('a')
        if not curr.children[i]:
            return False
        return self.helpSearch(word[1:], curr.children[i])
        
