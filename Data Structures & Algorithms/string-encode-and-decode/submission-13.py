class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            newS = str(len(s)) + "#" + s
            encoded += newS
        return encoded

    def decode(self, s: str) -> List[str]:
        results = []
        for i in range(len(s)):
            if s[i].isnumeric() and s[i+1] == "#":
                results.append(s[i+2:i+2+int(s[i])])
                i += 2 + int(s[i])
        return results