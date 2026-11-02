class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache = {}
        
        def dfs(index, prevInSeq):

            if index == len(nums):
                return 0

            if (index, prevInSeq) in cache:
                return cache[(index, prevInSeq)]

            result = 0
            if nums[index] <= prevInSeq:
                result = dfs(index+1, prevInSeq)
            else:
                result = max(dfs(index+1, nums[index])+1, dfs(index+1, prevInSeq))
            
            cache[(index, prevInSeq)] = result
            return result

        return dfs(0, float("-inf"))
            