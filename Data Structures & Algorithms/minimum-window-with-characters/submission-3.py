class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowMap = {}
        tMap = {}
        for char in t:
            if char in tMap:
                tMap[char] += 1
            else:
                tMap[char] = 1
            windowMap[char] = 0

        if len(s) < len(t):
            return ""

        start = 0
        while start < len(s) and s[start] not in tMap:
            start += 1

        matchesInWindow = 0
        result = ""
        end = start
        while end < len(s):
            if s[end] in windowMap:
                windowMap[s[end]] += 1
                if windowMap[s[end]] == tMap[s[end]]:
                    matchesInWindow += 1
                while matchesInWindow == len(tMap.keys()):
                    if not result or (end - start + 1) < len(result):
                        result = s[start:end+1]
                    if s[start] in windowMap:
                        windowMap[s[start]] -= 1
                        if windowMap[s[start]] < tMap[s[start]]:
                            matchesInWindow -= 1
                    start += 1
            end += 1

        return result


        