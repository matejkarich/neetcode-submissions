class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resLen = 0

        def expandFromCenter(l, r):
            nonlocal resLen, result
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                if (r-l+1) > resLen:
                    result = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1

        for i in range(len(s)):
            expandFromCenter(i, i)
            expandFromCenter(i, i+1)

        return result



