class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(index):
            
            if index == len(s):
                return True

            for w in wordDict:
                if w == s[index:index+len(w)]:
                    if dfs(index+len(w)):
                        return True

            return False


        return dfs(0)