class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        while start < end:
            currentSum = nums[start] + nums[end]
            if currentSum == target:
                return [start, end]
            elif currentSum > target:
                end -= 1
            else:
                start += 1