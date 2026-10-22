class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        charMap = {}
        for c in s1:
            if c in charMap:
                charMap[c] += 1
            else:
                charMap[c] = 1
        
        l, r = 0, len(s1)-1
        while r < len(s2):
            windowMap = {}
            while l < r:
                if s2[l] not in windowMap:
                    windowMap[s2[l]] = 1
                else:
                    windowMap[s2[l]] += 1
                l += 1
            if charMap == windowMap:
                return True
            r += len(s1)-1

        return False
