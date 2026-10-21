class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(index):
            if index >= len(nums):
                return 0

            if index in cache:
                return cache[index]

            robbed = 0
            for i in range(index+2, len(nums)):
                robbed = max(robbed, dfs(i))
            cache[index] = nums[index] + robbed
            return cache[index]

        result = 0
        for i in range(len(nums)):
            result = max(result, dfs(i))
        return result

        