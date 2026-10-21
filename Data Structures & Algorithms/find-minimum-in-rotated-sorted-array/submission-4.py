class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = float("inf")
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
                
            middle = (left + right) // 2
            result = min(result, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
            print(left)
            print(right)
            print()

        return result