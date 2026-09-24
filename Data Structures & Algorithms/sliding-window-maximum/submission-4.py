class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        i = 0
        while i < len(nums): # O(n - (n%k))
            if (i + k) > len(nums):
                break
            setK = nums[i:i+k] # O(k)
            heapq.heapify_max(setK) # O(log(k))
            result.append(heapq.heappop_max(setK))
            i += 1
        return result
        