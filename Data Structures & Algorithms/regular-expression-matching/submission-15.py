class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dfs(i, j):

            if i < 0 and j < 0:
                return True

            if j < 0:
                return False

            if p[j] == "*": # O(n^(n+m)) and could be simplified to O(2^(m+n))
                char = p[j-1]
                match = dfs(i, j-2)
                while i >= 0 and (s[i] == char or '.' == char):
                    i -= 1
                    match = match or dfs(i, j-2)
                return match or dfs(i, j-2)

            if i >= 0 and (s[i] == p[j] or p[j] == '.'):
                return dfs(i-1, j-1)

            return False

        return dfs(len(s)-1, len(p)-1)