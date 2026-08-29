class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.wordsInPath = 0

    def addWord(self, word):
        curr = self
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                newNode = TrieNode()
                newNode.wordsInPath = 1
                curr.children[index] = newNode
            else:
                curr.wordsInPath += 1
            curr = curr.children[index]
        curr.isEndOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()
        result = []

        for w in words:
            root.addWord(w)

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            index = ord(board[r][c])-ord('a')
            if board[r][c] == '*' or not node.children[index] or node.children[index].wordsInPath == 0:
                return

            letter = board[r][c]
            word += letter
            board[r][c] = '*'
            node = node.children[index]
            if node.isEndOfWord:
                result.append(word)
                node.wordsInPath -= 1

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            board[r][c] = letter 

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return result
        