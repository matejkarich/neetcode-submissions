class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = 0,len(nums)-1
        copy = nums.copy()
        copy.sort()
        print(copy)
        print(nums)
        finished = False
        copyIndexes = [i, j]
        while i < j and not finished:
            currSum = copy[i] + copy[j]
            if currSum == target:
                finished = True
                copyIndexes = [i, j]
            elif currSum < target:
                i += 1
            else:
                j -= 1
        if copy != nums:
            val1, val2 = copy[copyIndexes[0]], copy[copyIndexes[1]]
            if val1 != val2:
                return [nums.index(val1), nums.index(val2)]
            else:
                return sorted([nums.index(val1), nums.index(val2, nums.index(val1)+1)])
        else:
            return copyIndexes