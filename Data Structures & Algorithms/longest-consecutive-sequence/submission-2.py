class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        i = 0
        maxCount = 1
        while i < len(nums):
            print(nums[i])
            count = 1
            if (nums[i]-1) not in nset:
                val = nums[i] + 1
                while (val) in nset:
                    print(val)
                    count += 1
                    val += 1
            i += 1
            maxCount = max(maxCount, count)
            print(maxCount)
        return maxCount