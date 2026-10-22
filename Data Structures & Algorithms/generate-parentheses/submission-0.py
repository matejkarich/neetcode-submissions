class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = "(" * n + ")" * n
        return [parenthesis]
        # print(parenthesis)
