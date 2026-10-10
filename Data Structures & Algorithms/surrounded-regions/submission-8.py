class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        edges = set()
        q = deque()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == 0 or c == 0 or r == len(board)-1 or c == len(board[0])-1:
                    if board[r][c] == 'O':
                        q.append((r,c))
        # print(q)
        while q:
            cell = q.popleft()
            x,y = cell[0], cell[1]
            directions = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            for d in directions:
                if d[0] < 0 or d[0] <= len(board) or d[1] < 0 or d[1] < len(board[0]) or board[d[0]][d[1]] == 'X' or (d[0],d[1]) in visited:
                    continue
                q.append((d[0],d[1]))
            visited.add((x,y))
        # print(board)
        # for v in visited:
        #     print(v)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'

        