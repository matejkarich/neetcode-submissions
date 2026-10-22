class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            j = i
            while j != "#":
                j += 1
            val = int(s[i:j])
            res.append(s[i+2:i+val+2])
            print(res)
            i += val+2
        return res