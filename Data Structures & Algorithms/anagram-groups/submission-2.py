class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        
        for i in range(len(strs)):
            currentMap = defaultdict(int)
            skip = False
            for index in range(len(output)):
                if strs[i] in output[index]:
                    skip = True
            if skip:
                continue
            lst = [strs[i]]
            for char in strs[i]:
                currentMap[char] += 1
            print(currentMap)
            for j in range(i+1, len(strs)):
                comparingMap = defaultdict(int)
                for char in strs[j]:
                    comparingMap[char] += 1
                print(comparingMap)
                if currentMap == comparingMap:
                    lst.append(strs[j])
            output.append(lst)
        return output