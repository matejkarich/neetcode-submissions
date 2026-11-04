class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        grid = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(x, y):

            if x < 0 or x >= m or y < 0 or y >= n:
                return 0

            if grid[x][y] != -1:
                # grid[x][y] += 1
                return grid[x][y]

            if x == (m-1) and y == (n-1):
                return 1
 
            grid[x][y] = dfs(x+1,y) + dfs(x,y+1)
            return grid[x][y]

        return dfs(0,0)