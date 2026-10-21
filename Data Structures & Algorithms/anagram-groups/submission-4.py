class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        a1 = [strs[0]]
        for s in strs:
            added = False
            for arr in results:
                if Counter(s) == Counter(arr[0]):
                    arr.append(s)
                    added = True
                    break
            if not added:
                results.append([s])
        return results