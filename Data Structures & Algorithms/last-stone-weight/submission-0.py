class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while stones:
            print(stones)
            if len(stones) < 2:
                return stones[0]
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            print("x: " + str(x))
            print("y: " + str(y))
            if x > y:
                heapq.heappush_max(stones, x - y)
            print(stones)
            
        return 0