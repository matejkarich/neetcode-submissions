class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = defaultdict(int)
        map2 = defaultdict(int)
        for char in s:
            map[char] += 1
        for char in t:
            map2[char] += 1
        return map == map2
        