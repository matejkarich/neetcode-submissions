class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))


        time = 0
        while q:

            for _ in range(len(q)):
                cell = q.popleft()
                x,y = cell[0], cell[1]
                directions = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                for d in directions:
                    if d[0] < 0 or d[0] >= len(grid) or d[1] < 0 or d[1] >= len(grid[0]) or grid[d[0]][d[1]] != 1:
                        continue
                    q.append(d)
                grid[x][y] = 2

            time += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1

        return time-1
            



        