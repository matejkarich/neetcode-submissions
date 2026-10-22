class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = float("inf")
        left, right = 0, len(nums)-1

        if nums[left] < nums[right]:
            return nums[left]

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] >= nums[left]:
                left = middle + 1
                result = min(result, nums[left])
            else:
                right = middle - 1
                result = min(result, nums[left])
            print(left)
            print(right)
            print()

        return result