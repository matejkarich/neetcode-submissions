class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c, 0))

        while(q):
            cell = q.popleft()
            row, col, level = cell[0], cell[1], cell[2]
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue

            if grid[row][col] != 2147483647:
                if grid[row][col] == 0 and level == 0:
                    q.extend([(row-1,col,level+1), (row+1,col,level+1), (row,col-1,level+1), (row,col+1,level+1)])
                continue
            
            q.extend([(row-1,col,level+1), (row+1,col,level+1), (row,col-1,level+1), (row,col+1,level+1)])
            grid[row][col] = level
            

        