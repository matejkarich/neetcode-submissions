class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        cache = {}
        
        def dfs(index):
            
            if index == len(s):
                return True

            if index in cache:
                return cache[index]

            for w in wordDict:
                if w == s[index:index+len(w)]:
                    if dfs(index+len(w)):
                        cache[index+len(w)] = True
                        return True

            cache[index] = False
            return False


        return dfs(0)