class Solution:
    def numDecodings(self, s: str) -> int:
        
        result = 0
        cache = {}

        def dfs(index):

            if index == len(s):
                return 1

            if index > len(s) or s[index] == '0':
                return 0

            return dfs(index+1) + dfs(index+2)

        return dfs(0)