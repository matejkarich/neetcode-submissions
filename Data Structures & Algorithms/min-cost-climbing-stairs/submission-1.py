class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def dfs(stair):

            if stair in cache:
                return cache[stair] + cost[stair]

            if stair >= len(cost):
                return 0

            cache[stair] = min(dfs(stair+1), dfs(stair+2))
            return cache[stair] + cost[stair]


        return min(dfs(0), dfs(1))

            