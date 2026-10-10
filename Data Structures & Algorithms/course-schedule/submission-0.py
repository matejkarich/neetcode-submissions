class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependsOn = defaultdict(set)
        for c1,c2 in prerequisites:
            if c1 in dependsOn[c2]:
                return False
            dependsOn[c1].add(c2)
        return True
