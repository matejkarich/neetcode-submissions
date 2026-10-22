class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = 0,len(nums)-1
        copy = nums.copy()
        copy.sort()
        finished = False
        while i < j and not finished:
            currSum = nums[i] + nums[j]
            if currSum == target:
                finished = True
                copyIndexes = [i, j]
            elif currSum < target:
                i += 1
            else:
                j -= 1
        if copy != nums:
            return [copy.index(copyIndexes[0]), copy.index(copyIndexes[1])]
        else:
            return copyIndexes