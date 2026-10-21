class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums)-1, nums, target)

    def binarySearch(self, left, right, nums, target):
        middle = (left + right) // 2
        
        if left > right:
            return -1

        if nums[middle] == target:
            return middle

        elif nums[middle] > target:
            return self.binarySearch(left, middle-1, nums, target)
        
        else:
            return self.binarySearch(middle+1, right, nums, target)
        