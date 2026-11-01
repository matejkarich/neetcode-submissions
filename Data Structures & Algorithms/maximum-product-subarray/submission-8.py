class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxProd = nums[0]
        currMax = nums[0]
        currMin = nums[0]

        for i in range(1, len(nums)):

            # if nums[i] == 0:
            #     currMax = nums[i]
            #     currMin = 1
            #     maxProd = max(maxProd, currMax)
            #     continue
            
            temp = currMax * nums[i]
            temp2 = currMin * nums[i]
            currMax = max(temp, nums[i], temp2)
            currMin = min(temp2, nums[i], temp)
            maxProd = max(maxProd, currMax)

        return maxProd