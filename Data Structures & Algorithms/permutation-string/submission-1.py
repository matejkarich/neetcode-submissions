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
        
        l, r = 0, 0
        while r < len(s2):
            windowMap = {}
            while r-l <= len(s1)-1 and r < len(s2):
                # print("left: " + s2[l] + " right: " + s2[r])
                # print(windowMap)
                if s2[r] not in windowMap:
                    windowMap[s2[r]] = 1
                else:
                    windowMap[s2[r]] += 1
                print("left: " + s2[l] + " right: " + s2[r])
                print(windowMap)
                r += 1
            if charMap == windowMap:
                return True
            l += 1
            r = l

        return False
