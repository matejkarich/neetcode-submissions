class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        first, second = 0, len(s)-1
        while first < second:
            if not s[first].isalnum():
                first += 1
            if not s[second].isalnum():
                second -= 1
            if s[first] != s[second]:
                return False
            first += 1
            second -= 1
        return True