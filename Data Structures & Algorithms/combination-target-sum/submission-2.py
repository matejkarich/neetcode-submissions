class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combo = []

        def dfs(combo, index, runningSum):
            if runningSum == target:
                result.append(combo.copy())
                return

            if runningSum > target or index >= len(nums):
                return

            combo.append(nums[index])
            runningSum += nums[index]
            dfs(combo, index + 1, runningSum)
            dfs(combo, index, runningSum)


            combo.pop()
            runningSum -= nums[index]
            dfs(combo, index + 1, runningSum)


        dfs(combo, 0, 0)
        return [list(x) for x in set(tuple(x) for x in result)]