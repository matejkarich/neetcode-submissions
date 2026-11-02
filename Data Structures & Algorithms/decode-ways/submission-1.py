class Solution:
    def numDecodings(self, s: str) -> int:
        possibleCombos = []

        valueMap = {}
        for i in range(1, 27):
            valueMap[str(i)] = chr(ord('a') + (i - 1)).upper()
        print(valueMap)

        def dfs(index, prefix, combo):
            if index >= len(s):
                if prefix in valueMap:
                    if prefix != "":
                        combo.append(prefix)
                        possibleCombos.append(combo.copy())
                        combo.pop()
                    else:
                        possibleCombos.append(combo.copy())
                return

            if prefix+s[index] not in valueMap:
                return 
            combo.append(prefix+s[index])
            dfs(index+1, "", combo)
            combo.pop()
            prefix += s[index]
            dfs(index+1, prefix, combo)

        dfs(0, "", [])
        return len(possibleCombos)
                
