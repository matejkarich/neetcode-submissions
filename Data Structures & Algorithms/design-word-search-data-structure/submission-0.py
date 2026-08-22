class WordDictionary:

    def __init__(self):
        self.children = [None] * 27
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:
        if word == "":
            self.isEndOfWord = True
            return None
        indexOfChar = ord(word[0]) - 97
        if not self.children[indexOfChar]:
            self.children[indexOfChar] = WordDictionary()
        self.children[indexOfChar].addWord(word[1:])
        if not self.children[26]:
            self.children[26] = WordDictionary()
        self.children[26].addWord(word[1:])

    def search(self, word: str) -> bool:
        if word == "":
            return self.isEndOfWord
        if word[0] == ".":
            indexOfChar = 26
        else:
            indexOfChar = ord(word[0]) - 97
        nextTree = self.children[indexOfChar]
        if not nextTree:
            return False
        return nextTree.search(word[1:])
        