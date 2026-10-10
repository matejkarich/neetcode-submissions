class Solution:
    def solve(self, board: List[List[str]]) -> None:

        visited = set()
        # q = deque()

        # while q:

        #     for _ in range(len(q)):
        #         cell = q.popleft()
        #         x,y = cell[0], cell[1]
        #         directions = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        #         for d in directions:
        #             if (d[0] < 0 or d[0] >= len(board) or d[1] < 0 or d[1] >= len(board[0])):

        #             q.append(d)
        #             visited.add(d)

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
                if board[r][c] == 'O':
                    dfs(r,c,board)
        