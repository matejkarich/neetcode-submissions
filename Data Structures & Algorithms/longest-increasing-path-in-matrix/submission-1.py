class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        cache = {}

        def dfs(r, c):

            if (r,c) in cache:
                return cache[(r,c)]

            directions = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            longest = 1
            for d in directions:
                if d[0] < 0 or d[0] >= len(matrix) or d[1] < 0 or d[1] >= len(matrix[0]):
                    continue
                if matrix[d[0]][d[1]] > matrix[r][c]:
                    longest = max(longest, 1+dfs(d[0], d[1]))
            cache[(r,c)] = longest
            return longest

        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, dfs(r, c))
        return res
        