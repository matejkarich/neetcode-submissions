class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cache = {}

        def dfs(si, ti):

            if ti == len(t):
                return 1

            if si == len(s):
                return 0

            if (si, ti) in cache:
                return cache[(si,ti)]

            res = 0
            if s[si] == t[ti]:
                res = dfs(si+1, ti+1)
            
            cache[(si,ti)] = dfs(si+1, ti) + res
            return cache[(si,ti)]

        return dfs(0,0)

            
            