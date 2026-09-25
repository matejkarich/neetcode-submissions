class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        result = []
        i = 0
        while i <= len(nums)-k:  # O(n-k+1)
            j = 0
            while j < k:
                if i == 0:
                    heapq.heappush_max(maxHeap, (nums[j], j))
                elif j == k-1:
                    heapq.heappush_max(maxHeap, (nums[i+j], i+j))
                j += 1
            # print(maxHeap)

            top = maxHeap[0]
            while top[1] < i or top[1] >= i+j:
                top = heapq.heappop_max(maxHeap)
            result.append(top[0])
            i += 1
        return result


