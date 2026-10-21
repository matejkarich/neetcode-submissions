class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        s = s.lower()
        print(s[end].isalnum())
        while start < end:
            if not s[start].isalnum() and not s[end].isalnum():
                start += 1
                end -= 1
            elif not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            else: 
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
        return True