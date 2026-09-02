class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(combo, index, runningSum):
            if runningSum == target:
                result.append(combo.copy())
                return
            if runningSum > target or index >= len(candidates):
                return

            combo.append(candidates[index])
            dfs(combo, index + 1, runningSum + candidates[index])
            combo.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(combo, index + 1, runningSum)

        dfs([], 0, 0)
        return result