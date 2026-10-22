class Solution:
    def longestPalindrome(self, s: str) -> str:

        cache = {}
        
        def isPalindrome(w):
            i,j = 0, len(w)-1
            while i < j:
                if w[i] != w[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(start, end):

            if start > end:
                return ""

            word = s[start:end+1]

            if word in cache:
                return cache[word]

            if isPalindrome(word):
                return word
            
            w1 = dfs(start+1, end)
            cache[w1] = w1
            w2 = dfs(start, end-1)
            cache[w2] = w2
            if len(w1) > len(w2):
                return w1
            return w2

        return dfs(0,len(s)-1)

        