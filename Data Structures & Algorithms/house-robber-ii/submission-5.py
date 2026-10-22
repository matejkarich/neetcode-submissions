class Solution:
    def rob(self, nums: List[int]) -> int:
        # cache = [[-1, -1]] * len(nums)
        cache = [[-1, -1] for _ in range(len(nums))]

        def dfs(houseIndex, robbedFirst):

            if houseIndex >= len(nums):
                return 0

            if houseIndex == len(nums)-1 and robbedFirst:
                return 0

            if cache[houseIndex][robbedFirst] != -1:
                return cache[houseIndex][robbedFirst]

            if houseIndex == 0:
                robCurrent = nums[houseIndex] + dfs(houseIndex+2, True)
            else:
                robCurrent = nums[houseIndex] + dfs(houseIndex+2, robbedFirst)
            skipCurrent = dfs(houseIndex+1, robbedFirst)
            cache[houseIndex][robbedFirst] = max(robCurrent, skipCurrent)
            return cache[houseIndex][robbedFirst]

        return dfs(0, False)

            