class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        maxCount = 1
        characterCount = {}

        if len(s) < 2:
            return len(s)

        characterCount[s[l]] = 1
        while r < len(s):
            if s[r] in characterCount:
                characterCount[s[r]] += 1
            else:
                characterCount[s[r]] = 1
            
            mostFrequentChar = self.findLargestInMap(characterCount)
            countOfCharsToRemove = (r-l+1) - characterCount[mostFrequentChar]
            if countOfCharsToRemove - k > 0:
                while l < r:
                    characterCount[s[l]] -= 1
                    l += 1

                    mostFrequentChar = self.findLargestInMap(characterCount)
                    countOfCharsToRemove = (r-l+1) - characterCount[mostFrequentChar]

                    if countOfCharsToRemove - k <= 0:
                        r += 1
                        break
            else:
                maxCount = max(maxCount, r-l+1)
                r += 1

        return maxCount


    def findLargestInMap(self, countMap):
        largest = ""
        maxCount = 0
        for letter, count in countMap.items():
            if count > maxCount:
                maxCount = count
                largest = letter
        return largest


