class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        for index, num in enumerate(nums):
            map[num] = index
        for i in range(len(nums)):
            check = target - nums[i]
            if check in map and i != map[check]:
                return [i, map[check]]