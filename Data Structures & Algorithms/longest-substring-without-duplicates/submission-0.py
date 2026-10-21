class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characterCount = {}

        if len(s) < 2:
            return len(s)

        l,r = 0,1
        characterCount[s[l]] = l
        maxCount = 1
        while l < r and r < len(s):

            if s[r] not in characterCount or characterCount[s[r]] < l:
                maxCount = max(maxCount, r-l+1)
                characterCount[s[r]] = r
                r += 1
                
            else:
                previousIndex = characterCount[s[r]]
                characterCount[s[r]] = r
                if s[l] == s[r]:
                    l += 1
                    r += 1
                else:
                    l = previousIndex + 1
                    r += 1
            

        return maxCount
