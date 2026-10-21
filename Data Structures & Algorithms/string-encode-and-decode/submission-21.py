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
            value = ""
            while s[i].isnumeric():
                value += s[i]
                i += 1
            print(value)
            results.append(s[i+1:i+1+int(value)])
            i += int(value) + 1
            print(results)
        return results