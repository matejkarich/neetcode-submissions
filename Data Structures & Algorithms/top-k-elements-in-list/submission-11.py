class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        order = []
        for key, val in counter.items():
            order.append((key, val))
        order.sort(key=lambda x: x[1])
        result = []
        i = 0
        while i != k:
            result.append(order[-1-i][0])
            i += 1
        return result
