class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(paren, n, op, close):
            if n == 0:
                if op == close:
                    result.append("".join(paren.copy()))
                return

            if close > op:
                return

            paren.append(')')
            dfs(paren, n - 1, op, close + 1)
            paren.pop()

            paren.append('(')
            dfs(paren, n - 1, op + 1, close)
            paren.pop()

        
        dfs([], 2*n, 0, 0)
        return result


        