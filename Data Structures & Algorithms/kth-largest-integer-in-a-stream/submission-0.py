class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = []
        for num in nums:
            if len(data) > k:
                heapq.heappop(data)
            heapq.heappush(data, num)
        

    def add(self, val: int) -> int:
        heapq.pop(self.data)
        heapq.push(self.data, val)
        return self.data[0]
