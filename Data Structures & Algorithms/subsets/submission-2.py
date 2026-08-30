class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        def dfs(subset, index):
            if index >= len(nums):
                return
            subset.append(nums[index])
            # results.append(subset)
            for i in range(index+1, len(nums)):
                results.append(subset + [nums[i]])
            for j in range(index + 1, len(nums)):
                dfs(subset, j)
            

        for idx, num in enumerate(nums):
            subset = []
            dfs(subset, idx)
            results.append([num])
        
        return results