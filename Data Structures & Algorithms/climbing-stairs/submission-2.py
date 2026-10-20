class Solution:
    def climbStairs(self, n: int) -> int:
        
        uniqueCount = {}

        def dfs(step):

            if step in uniqueCount:
                return uniqueCount[step]

            if step > n:
                return 0

            if step == n:
                return 1

            if (step+1) in uniqueCount and (step+2) in uniqueCount:
                uniqueCount[step] = uniqueCount[step+1] + uniqueCount[step+2]
            elif (step+1) in uniqueCount:
                uniqueCount[step] = uniqueCount[step+1] + dfs(step+2)
            elif (step+2) in uniqueCount:
                uniqueCount[step] = dfs(step+1) + uniqueCount[step+2]
            else:
                uniqueCount[step] = dfs(step+1) + dfs(step+2)

            return uniqueCount[step]

        return dfs(0)

            
