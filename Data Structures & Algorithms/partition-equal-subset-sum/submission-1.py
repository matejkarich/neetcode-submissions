class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        cache = {}

        def dfs(index, s1, s2):

            if index == len(nums):
                return sum(s1) == sum(s2)

            if (index,sum(s1),sum(s2)) in cache:
                return cache[(index,sum(s1),sum(s2))]

            cache[(index,sum(s1),sum(s2))] = dfs(index+1, s1 + [nums[index]], s2) or dfs(index+1, s1, s2 + [nums[index]])
            return cache[(index,sum(s1),sum(s2))]

        return dfs(0, [], [])

