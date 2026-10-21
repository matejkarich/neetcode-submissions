class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
            elif temp <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temp > temperatures[stack[-1]]: 
                    removeIndex = stack.pop()
                    result[removeIndex] = i - removeIndex
                stack.append(i)
        return result

