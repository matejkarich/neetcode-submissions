class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        for i in range(len(nums)-1):
            prefix.append(nums[i]*prefix[i])
        for i in range(len(nums)-1, 0, -1):
            suffix.insert(0, nums[i]*suffix[0])
        print(prefix)
        print(suffix)
        return [prefix[i]*suffix[i] for i in range(len(prefix))]