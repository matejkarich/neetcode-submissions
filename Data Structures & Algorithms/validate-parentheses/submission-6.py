class Solution:
    def isValid(self, s: str) -> bool:
        mapParenth = {'(': ')', '{':'}', '[':']'}
        stack = []
        for char in s:
            if char in mapParenth.keys():
                stack.append(char)
            else:
                if stack:
                    popped = stack.pop()
                    if (mapParenth[popped] != char):
                        return False
                else:
                    return False
        if stack:
            return False
        return True