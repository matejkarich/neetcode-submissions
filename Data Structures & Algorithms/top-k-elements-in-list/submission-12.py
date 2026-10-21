class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        ordered = [[] for i in range(len(nums)+1)]
        result = []
        print(counter)
        print(ordered)
        for num, count in counter.items():
            ordered[count].append(num)
        for i in range(len(ordered)-1, -1, -1):
            for num in ordered[i]:
                result.append(num)
                if len(result) == k:
                    return result
