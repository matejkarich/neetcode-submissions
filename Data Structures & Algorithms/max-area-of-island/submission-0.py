class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(x, y, grid):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0

            grid[x][y] = 0
            result = dfs(x-1, y, grid) + dfs(x+1, y, grid) + dfs(x, y-1, grid) + dfs(x, y+1, grid) + 1
            return result

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maxArea = max(maxArea, dfs(r, c, grid))
        return maxArea
            
        