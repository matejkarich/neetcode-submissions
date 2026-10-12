class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {i:[] for i in range(n)}

        for edge in edges:
            edgeMap[edge[0]].append(edge[1])

        print(edgeMap)

        def dfs(edge, visited):
            print(visited)
            if edge in visited:
                return False

            if len(edgeMap[edge]) == 0:
                visited.add(edge)
                return True
            
            visited.add(edge)
            for e in edgeMap[edge]:
                res = dfs(e, visited)
                if not res:
                    return False
            return True

        
        for edge in edgeMap.keys():
            visited = set()
            res = dfs(edge, visited)
            if not res:
                return False
        return True