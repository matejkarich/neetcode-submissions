class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        visited = set()

        def dfs(board, r, c, remainingQ):

            if r < 0 or r >= len(board[0]) or c < 0 or c >= len(board) or (r,c) in visited:
                return

            visited.add((r,c))
            if not self.canAttack(board, r, c):
                board[r][c] = "Q"
                remainingQ -= 1

                if remainingQ == 0:
                    result.append(["".join(row) for row in board])
                    board[r][c] = "."
                    remainingQ += 1
                    visited.remove((r,c))
                    return

            dfs(board, r, c-1, remainingQ)
            dfs(board, r, c+1, remainingQ)
            dfs(board, r-1, c-1, remainingQ)
            dfs(board, r-1, c, remainingQ)
            dfs(board, r-1, c+1, remainingQ)
            dfs(board, r+1, c-1, remainingQ)
            dfs(board, r+1, c, remainingQ)
            dfs(board, r+1, c+1, remainingQ)

            visited.remove((r,c))
            if board[r][c] == "Q":
                remainingQ += 1
                board[r][c] = "."
        
        for r in range(n):
            for c in range(n):
                board = [["."]*n for _ in range(n)]
                dfs(board, r, c, n)

        return result
            
        
    def canAttack(self, board, r, c):

        def canAttackRow():
            if 'Q' in board[r]:
                return True
            return False

        def canAttackCol():
            for i in range(len(board)):
                if 'Q' in board[i][c]:
                    return True
            return False

        def canAttackDiag():
            for i in range(len(board)):
                if r - i >= 0:
                    if c - i >= 0 and 'Q' == board[r-i][c-i]:
                        return True
                    if c + i < len(board) and 'Q' == board[r-i][c+i]:
                        return True
                if r + i < len(board[r]):
                    if c - i >= 0 and 'Q' == board[r+i][c-i]:
                        return True
                    if c + i < len(board) and 'Q' == board[r+i][c+i]:
                        return True
            return False

        return canAttackRow() or canAttackCol() or canAttackDiag()