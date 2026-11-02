class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            temp = currSum * nums[i]
            if temp < nums[i]:
                currSum = nums[i]
            else:
                currSum = temp

            if currSum > maxSum:
                maxSum = currSum

        return maxSum