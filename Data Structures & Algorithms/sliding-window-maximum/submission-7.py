class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        result = []
        i = 0
        while i <= len(nums)-k:  # O(n-k+1)
            j = 0
            while j < k:
                heapq.heappush_max(maxHeap, (nums[i+j], i+j))
                j += 1            
            top = heapq.heappop_max(maxHeap)
            while top[1] < i or top[1] >= i+j:
                top = heapq.heappop_max(maxHeap)
            result.append(top[0])
            i += 1
        return result


