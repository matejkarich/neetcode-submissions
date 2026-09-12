class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = []
        for num in nums:
            if len(self.data) >= k:
                heapq.heappop(self.data)
            heapq.heappush(self.data, num)
        print(self.data)
        

    def add(self, val: int) -> int:
        print(self.data)
        heapq.heappop(self.data)
        heapq.heappush(self.data, val)
        return self.data[0]
