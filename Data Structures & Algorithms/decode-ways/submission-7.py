class Solution:
    def numDecodings(self, s: str) -> int:
        
        result = 0
        cache = {}

        def dfs(index):

            if index in cache:
                return cache[index]

            if index == len(s):
                return 1

            if index > len(s) or s[index] == '0':
                return 0

            oneChar = dfs(index+1)
            twoChar = 0
            if 10 <= int(s[index:index+2]) <= 26:
                twoChar = dfs(index+2)

            cache[index] = oneChar + twoChar
            return cache[index]

        return dfs(0)