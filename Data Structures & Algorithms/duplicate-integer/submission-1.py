class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = Counter(nums)
        for key, value in dic.items():
           if value > 1:
               return True
        return False