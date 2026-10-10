from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(start_r, start_c):
            stack = [(start_r, start_c)]
            visited.add((start_r, start_c))

            region = []
            surrounded = True

            while stack:
                r, c = stack.pop()
                region.append((r, c))

                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    surrounded = False

                for nr, nc in (
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1),
                ):
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and board[nr][nc] == 'O'
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        stack.append((nr, nc))

            return surrounded, region

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    surrounded, region = dfs(r, c)

                    if surrounded:
                        for region_r, region_c in region:
                            board[region_r][region_c] = 'X'