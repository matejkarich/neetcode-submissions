class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        result = []
        start = 0
        for i in range(k):
            heapq.heappush_max(maxHeap, (nums[i], i))
        
        while start <= len(nums) - k:
            top = maxHeap[0]
            while top[1] < start:
                heapq.heappop_max(maxHeap)
                top = maxHeap[0]
            result.append(top[0])
            if start + k < len(nums):
                heapq.heappush_max(maxHeap, (nums[start+k], start+k))
            start += 1
        return result
            
                
        