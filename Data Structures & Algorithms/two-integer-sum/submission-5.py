class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = 0,len(nums)-1
        copy = nums.copy()
        copy.sort()
        print(copy)
        print(nums)
        while i < j:
            currSum = nums[i] + nums[j]
            if currSum == target:
                return [i, j]
            elif currSum < target:
                i += 1
            else:
                j -= 1