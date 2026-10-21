class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                second = stack.pop()
                first = stack.pop()
                result = eval(str(first) + token + str(second))
                stack.append(int(result))
        return int(stack.pop())