class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def expandOutward(l, r):
            nonlocal result

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                result += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expandOutward(i, i)
            expandOutward(i, i+1)

        return result