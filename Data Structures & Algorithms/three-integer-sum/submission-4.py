class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indices = []
        for i in range(len(nums)):
            first = nums[i]
            target = 0 - first
            nmap = {}
            for index, val in enumerate(nums):
                if index <= i:
                    continue
                nmap[val] = index
            for j in range(i+1, len(nums)):
                val = target - nums[j]
                index = sorted([first, nums[j], val])
                if val in nmap and j != nmap[val] and index not in indices:  
                    indices.append(index)
        return indices
            