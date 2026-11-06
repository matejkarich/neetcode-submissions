class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = {}
        
        def dfs(i, remAmount):

            if (i, remAmount) in cache:
                return cache[(i,remAmount)]

            if i == len(nums):
                return remAmount == 0

            cache[(i,remAmount)] = dfs(i+1, remAmount-nums[i]) + dfs(i+1, remAmount+nums[i])
            return cache[(i,remAmount)]

        return dfs(0, target)