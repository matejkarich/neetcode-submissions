class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0

        def dfs(x, y, grid, count):

            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or "0" == grid[x][y] or "X" == grid[x][y]:
                return 0
            count += 1
            grid[x][y] = "X"
            dfs(x - 1, y, grid, count)
            dfs(x + 1, y, grid, count)
            dfs(x, y - 1, grid, count)
            dfs(x, y + 1, grid, count)

            if count > 0:
                return 1


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                numIslands += dfs(r, c, grid, 0)
        return numIslands
            
        