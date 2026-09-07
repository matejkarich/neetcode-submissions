class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p', 'q', 'r','s'], 8:['t','u','v'], 9:['w','x','y','z']}

        result = []
        if len(digits) == 0:
            return result

        def dfs(letterCombo, index):
            if index >= len(digits):
                    result.append(letterCombo)
                    return

            for letter in letterMap[int(digits[index])]:
                dfs(letterCombo + letter, index+1)

        dfs("", 0)
        return result

        