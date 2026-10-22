class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        result = []
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
                    counts.pop(-1)
                    result.append(key)
            k -= 1
        return result
            