class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(index):
            if index >= len(nums):
                return 0

            if index in cache:
                return cache[index]

            robCurrent = dfs(index+2) + nums[index]
            skipCurrent = dfs(index+1)
            cache[index] = max(robCurrent, skipCurrent)
            return cache[index]

        return dfs(0)

        