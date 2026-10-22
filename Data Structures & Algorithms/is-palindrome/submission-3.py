class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        first, second = 0, len(s)-1
        while first < second:
            while not s[first].isalnum():
                first += 1
            while not s[second].isalnum():
                second -= 1
            if not first < second:
                break
            if s[first] != s[second]:
                return False
            first += 1
            second -= 1
        return True