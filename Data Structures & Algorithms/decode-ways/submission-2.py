class Solution:
    def numDecodings(self, s: str) -> int:
        possibleCombos = set()

        valueMap = {}
        for i in range(1, 27):
            valueMap[str(i)] = chr(ord('a') + (i - 1)).upper()
        print(valueMap)

        def dfs(index, prefix, combo):
            if index >= len(s):
                if prefix != "" and prefix in valueMap:
                    combo.append(prefix)
                    possibleCombos.add(tuple(combo))
                    combo.pop()
                else:
                    possibleCombos.add(tuple(combo))
                return

            if prefix+s[index] not in valueMap:
                return 
            combo.append(prefix+s[index])
            dfs(index+1, "", combo)
            combo.pop()
            prefix += s[index]
            dfs(index+1, prefix, combo)

        dfs(0, "", [])
        print(possibleCombos)
        return len(possibleCombos)
                
