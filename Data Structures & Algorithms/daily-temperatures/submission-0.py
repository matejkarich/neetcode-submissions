class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        index = len(temperatures) - 2
        while len(temperatures) > 1:
            previous = temperatures.pop()
            if temperatures[-1] < previous:
                result[index] = 1
            else:
                result[index] = result[index+1] + 1 if result[index+1] > 0 else 0
            index -= 1
        return result

