class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        firstK = nums[:k].copy()
        heapq.heapify(firstK)
        for num in nums[k:]:
            if num > firstK[0]:
                heapq.heappushpop(firstK, num)
        return firstK[0]