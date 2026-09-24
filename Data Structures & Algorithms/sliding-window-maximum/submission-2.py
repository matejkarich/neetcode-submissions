class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        i = 0
        while i < len(nums): # O(n - (k-1))
            if (i + k) > len(nums):
                break
            setK = nums[i:i+k] # O(k)
            result.append(max(setK)) # O(k)
            i += 1
        return result
        