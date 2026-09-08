class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []

        def dfs(part, pStart, i):
            if i >= len(s):
                if pStart >= i:
                    result.append(part)
                return
            
            if isPal(s[pStart:i+1]):
                part.append(s[pStart:i+1])
                dfs(part, i+1, i+1)
                part.pop()
            dfs(part, pStart, i+1)

        
        