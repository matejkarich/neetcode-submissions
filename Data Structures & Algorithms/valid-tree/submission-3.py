class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {i:[] for i in range(n)}
        visited = set()

        for edge in edges:
            edgeMap[edge[0]].append(edge[1])
            edgeMap[edge[1]].append(edge[0])

        print(edgeMap)

        def dfs(edge, parent, visited):
            print(visited)
            if edge in visited:
                return False
            
            visited.add(edge)
            for e in edgeMap[edge]:
                if e == parent:
                    continue
                res = dfs(e, edge, visited)
                if not res:
                    return False
            return True

        res = dfs(0, -1, visited)
        if not res:
            return False
        for edge in edgeMap.keys():
            if edge not in visited:
                return False
        return True