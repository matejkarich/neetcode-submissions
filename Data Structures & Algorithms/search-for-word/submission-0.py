class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, curr):
            if r >= ROWS or c >= COLS or board[r][c] == '*' or len(curr) > len(word):
                return False

            if curr == word:
                return True

            temp = board[r][c]
            curr += temp
            board[r][c] = '*'
            up = dfs(r - 1, c, curr)
            down = dfs(r + 1, c, curr)
            left = dfs(r, c - 1, curr)
            right = dfs(r, c + 1, curr)
            board[r][c] = temp

            return up or down or left or right

        result = False
        for r in range(ROWS):
            for c in range(COLS):
                result = result or dfs(r, c, "")
        return result