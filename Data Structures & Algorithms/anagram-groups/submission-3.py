class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            charCount = [0] * 26
            for char in string:
                index = ord(char) - ord("a")
                charCount[index] += 1
            result[tuple(charCount)].append(string)
        return result.values()