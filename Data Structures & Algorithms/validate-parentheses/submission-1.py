class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', "{", "["]
        for char in s:
            if char in opening:
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
        return len(stack) == 0