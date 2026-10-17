class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited = set()
        for edge in edges:
            if edge[0] in visited and edge[1] in visited:
                return edge
            visited.add(edge[0])
            visited.add(edge[1])
        return None
        