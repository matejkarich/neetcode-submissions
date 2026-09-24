class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        i = 0
        while i < len(nums): # O(n - (n%k))
            if (i + k) > len(nums):
                break
            setK = nums[i:i+k] # O(k)
            setK.sort() # O(k * log(k))
            result.append(setK[-1])
            i += 1
        return result
        