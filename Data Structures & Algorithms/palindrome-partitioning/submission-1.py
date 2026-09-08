class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []

        def dfs(part, pStart, i):
            if i >= len(s):
                if pStart >= i:
                    result.append(part.copy())
                return
            
            if self.isPal(s[pStart:i+1]):
                part.append(s[pStart:i+1])
                dfs(part, i+1, i+1)
                part.pop()
            dfs(part, pStart, i+1)
        
        dfs([], 0, 0)
        return result

    def isPal(self, s):
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
            
        return True

        
        