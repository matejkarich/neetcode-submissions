class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            runningSum = numbers[start] + numbers[end]
            if runningSum == target:
                return [start+1, end+1]
            elif runningSum < target:
                start += 1
            else:
                end -= 1
            