class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(subset, index):
            if index == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[index])
            dfs(subset, index + 1)

            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1

            
            subset.pop()
            dfs(subset, index + 1)

        dfs([], 0)
        return result