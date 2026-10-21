class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, second = 0, len(numbers)-1
        while first < second:
            val = numbers[first] + numbers[second]
            if val == target:
                return [first+1, second+1]
            elif val < target:
                first += 1
            else:
                second -= 1
        return []