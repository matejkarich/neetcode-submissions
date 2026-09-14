class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.distanceToOrigin(pair[0], pair[1]), [pair[0], pair[1]]) for pair in points]
        heapq.heapify(distances)
        result = [heapq.heappop(distances)[1] for _ in range(k)]
        print(result)
        return result

    def distanceToOrigin(self, x, y):
        return math.sqrt(x**2 + y**2)
        