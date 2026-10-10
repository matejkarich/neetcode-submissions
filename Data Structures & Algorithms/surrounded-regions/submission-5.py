class Solution:
    def solve(self, board: List[List[str]]) -> None:

        visited = set()

        def dfs(r, c, board, region):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if board[r][c] == 'X' or (r,c) in visited:
                return True

            visited.add((r,c))
            region.append((r,c))
            return dfs(r-1,c,board, region) and dfs(r+1,c,board, region) and dfs(r,c-1,board, region) and dfs(r,c+1,board, region)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r,c) not in visited:
                    region = []
                    surrounded = dfs(r,c,board, region)
                    if surrounded:
                        for pair in region:
                            board[pair[0]][pair[1]] = 'X'
        