class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tMap = {}
        for char in t:
            if char not in tMap:
                tMap[char] = 1
            else:
                tMap[char] += 1

        l, r = 0, 0
        val = ""
        windowMap = {}

        while l < r and r < len(s):
            if l < len(s) and s[l] not in tMap:
                l += 1
                r = l if r == 0 else r
            else:
                if s[r] in tMap:
                    if s[r] not in windowMap:
                        windowMap[s[r]] = 1
                    else:
                        windowMap[s[r]] += 1
                print(s[l:r+1])
                print(windowMap)
                if self.charactersContained(windowMap, tMap):
                    currVal = s[l:r+1]
                    # print(currVal)
                    if len(val) == 0 or len(currVal) < len(val):
                        val = currVal
                    if s[l] in windowMap:
                        windowMap[s[l]] -= 1
                    l += 1
                if r < len(s):
                    r += 1
            

        return val

    def charactersContained(self, windowMap, tMap):
        for key, value in tMap.items():
            if key not in windowMap or windowMap[key] < value:
                return False
        return True

