class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle_index = len(nums) // 2
        if len(nums) == 0:
            return -1
        if nums[middle_index] == target:
            return middle_index
        elif nums[middle_index] > target:
            return self.search(nums[0:middle_index], target)
        else:
            return self.search(nums[middle_index+1:], target)
        