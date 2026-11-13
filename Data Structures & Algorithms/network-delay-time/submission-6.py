class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        dist = [0] + [float("inf")] * n + [0]
        heap = []

        graph = {i:[] for i in range(1,n+1)}
        for time in times:
            u,v,t = time[0], time[1], time[2]
            graph[u].append((v,t))

        dist[k] = 0
        heapq.heappush(heap, (dist[k], k))

        while heap:
            udist, u = heapq.heappop(heap)

            if udist > dist[u]:
                continue

            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
                    
        maxDist = float("-inf")
        for d in dist:
            if d == float("inf"):
                return -1
            maxDist = max(maxDist, d)

        return maxDist