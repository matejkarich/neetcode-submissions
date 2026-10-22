class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def dfs(houseIndex, robbedFirst):

            if houseIndex >= len(nums):
                return 0

            if houseIndex == len(nums)-1 and robbedFirst:
                return 0

            if cache[houseIndex] != -1:
                return cache[houseIndex]

            robCurrent = nums[houseIndex] + dfs(houseIndex+2, robbedFirst)
            skipCurrent = dfs(houseIndex+1, False)
            return max(robCurrent, skipCurrent)

        return dfs(0, True)

            