class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dfs(subset, index):
            if index == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[index])
            dfs(subset, index + 1)
            
            subset.pop()
            dfs(subset, index + 1)

        dfs(subset, 0)
        return result