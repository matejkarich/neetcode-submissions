class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = {i:[] for i in range(numCourses)}
        order = []

        def dfs(course, visited):
            if len(prereqMap[course]) == 0:
                if course not in order:
                    order.append(course)
                return True
            if course in visited:
                return False

            visited.add(course)
            for prereq in prereqMap[course]:
                res = dfs(prereq, visited)
                if not res:
                    return False
            visited.remove(course)
            order.append(course)
            prereqMap[course] = []
            return True

        for p in prerequisites:
            prereqMap[p[0]].append(p[1])

        for c in range(numCourses):
            visited = set()
            res = dfs(c, visited)
            if not res:
                return []
        return order

