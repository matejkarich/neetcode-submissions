class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = []
        self.k = k
        for num in nums:
            if len(self.data) >= k:
                heapq.heappushpop(self.data, num)
            else:
                heapq.heappush(self.data, num)
        print(self.data)
        

    def add(self, val: int) -> int:
        print(self.data)
        if len(self.data) >= self.k:
            heapq.heappushpop(self.data, val)
        else:
            heapq.heappush(self.data, val)
        return self.data[0]
