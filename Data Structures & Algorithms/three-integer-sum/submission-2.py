class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indices = []
        ignore = []
        for i in range(len(nums)):
            first = nums[i]
            target = 0 - first
            nmap = {}
            for index, val in enumerate(nums):
                if index <= i:
                    continue
                nmap[val] = index
            for j in range(i+1, len(nums)):
                print(nmap)
                val = target - nums[j]
                if val in nmap and nmap[val] not in ignore and j != nmap[val]:
                    ignore.append(nmap[val])
                    ignore.append(nmap[nums[j]])
                    #nmap.pop(val)
                    indices.append([first, nums[j], val])
                print(ignore)
        return indices
            