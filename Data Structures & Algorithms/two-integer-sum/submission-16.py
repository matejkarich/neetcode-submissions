class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}
        for i, n in enumerate(nums):
            indexMap[n] = i

        for index, val in enumerate(nums):
            diff = target - val
            if diff in indexMap and index != indexMap[diff]:
                return [index, indexMap[diff]]
        
        return []