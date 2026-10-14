class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {i:[] for i in range(n)}
        visited = set()

        for edge in edges:
            edgeMap[edge[0]].append(edge[1])

        print(edgeMap)

        def dfs(edge, visited):
            print(visited)
            if edge in visited:
                return False
            
            visited.add(edge)
            for e in edgeMap[edge]:
                res = dfs(e, visited)
                if not res:
                    return False
            return True

        res = dfs(0, visited)
        if not res:
            return False
        for edge in edgeMap.keys():
            if edge not in visited:
                return False
        return True