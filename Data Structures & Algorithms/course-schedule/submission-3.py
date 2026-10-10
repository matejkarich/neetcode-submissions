class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            preMap[c].append(p)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if len(preMap[course]) == 0:
                return True
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            return True
        
        for c in preMap.keys():
            if not dfs(c):
                return False
        return True