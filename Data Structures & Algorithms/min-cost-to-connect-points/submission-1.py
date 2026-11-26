class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = {}
        for f in range(len(points)):
            adjList[f] = []
            for s in range(len(points)):
                if f == s:
                    continue
                i, j = points[f], points[s]
                d = abs(j[0]-i[0]) + abs(j[1]-i[1])
                adjList[f].append((d, s))
            adjList[f].sort()

        #print(adjList)

        visited = set()
        queue = [[0,0]]
        pathLen = 0
        while queue:
            v = heapq.heappop(queue)
            if v[1] in visited:
                continue
            visited.add(v[1])
            pathLen += v[0]
            for q in adjList[v[1]]:
                heapq.heappush(queue, q)
        
        return pathLen
            

            