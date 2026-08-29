class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

    def addWord(self, word):
        curr = self
        for char in word:
            i = ord(char) - ord('a')
            if not curr.children[i]:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.isEndOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])
        result, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                (r,c) in visit or 
                not node.children[ord(board[r][c]) - ord('a')]):
                return

            index = ord(board[r][c]) - ord('a')
            visit.add((r,c))
            word += board[r][c]
            node = node.children[index]
            if node.isEndOfWord:
                result.add(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(result)