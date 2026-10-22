class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set()
        for num in nums:
            store.add(num)
        maxLen = 1
        for num in nums:
            currentLen = 1
            while (num+1) in store:
                num += 1
                currentLen += 1
            maxLen = max(maxLen, currentLen)
        return maxLen
        