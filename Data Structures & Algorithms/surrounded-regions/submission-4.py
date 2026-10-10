class Solution:
    def solve(self, board: List[List[str]]) -> None:

        visited = set()

        def dfs(r, c, board):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if board[r][c] == 'X' or (r,c) in visited:
                return True

            visited.add((r,c))
            result = dfs(r-1,c,board) and dfs(r+1,c,board) and dfs(r,c-1,board) and dfs(r,c+1,board)
            if result:
                board[r][c] = 'X'
            return result

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r,c) not in visited:
                    dfs(r,c,board)
        