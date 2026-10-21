class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = defaultdict(int)
        result = set()
        for num in nums:
            count[num] += 1
        counts = list(count.values())
        counts.sort()
        print(counts)
        print(count.items())
        while k > 0:
            for key, val in count.items():
                print(key, val)
                if val == counts[-1]:
                    print(counts)
                    result.add(key)
            counts.pop(-1)
            k -= 1
        return list(result)
            