class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(permutation, remainingNums):
            if len(remainingNums) == 0:
                result.append(permutation.copy())
                return

            for i in range(len(remainingNums)):
                permutation.append(remainingNums[i])
                dfs(permutation, remainingNums[:i]+remainingNums[i+1:])
                permutation.pop()

        dfs([], nums)
        return result
        