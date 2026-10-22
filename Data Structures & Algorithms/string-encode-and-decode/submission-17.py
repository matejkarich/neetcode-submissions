class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            newS = str(len(s)) + "#" + s
            encoded += newS
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        results = []
        i = 0
        while i < len(s):
            value = 0
            while s[i] != "#":
                value += int(s[i])
                i += 1
            results.append(s[i+1:i+1+value])
            i += value + 1
            print(results)
        return results