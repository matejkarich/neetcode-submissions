class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i:[] for i in range(n)}
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for edge in graph[node]:
                dfs(edge)

        connected = 0
        for i in range(n):
            if i in visited:
                continue
            connected += 1
            dfs(i)
        return connected