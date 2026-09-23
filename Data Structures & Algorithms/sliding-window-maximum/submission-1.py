class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        i = 0
        while i < len(nums):
            if (i + k) > len(nums):
                break
            setK = nums[i:i+k]
            setK.sort()
            result.append(setK[-1])
            i += 1
        return result
        