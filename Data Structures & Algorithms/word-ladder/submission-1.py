class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: # O(n)
            return 0

        graph = {w:[] for w in wordList}
        graph[beginWord] = []

        def canTransition(w1, w2): # O(m)
            sharedCount = 1
            i = 0
            while i < len(w1) and i < len(w2):
                if w1[i] != w2[i]:
                    sharedCount -= 1
                if sharedCount < 0:
                    return False
                i += 1
            if sharedCount == 1:
                i += 1
            if i < len(w1) or i < len(w2):
                return False
            return True

        for i in range(len(wordList)): # O(n*m*n*m) = O(n^2 * m^2)
            for j in range(i+1, len(wordList)):
                if canTransition(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
            if canTransition(beginWord, wordList[i]):
                graph[wordList[i]].append(beginWord)
                graph[beginWord].append(wordList[i])

        q = deque()
        visited = set()
        q.append(beginWord)
        minWords = 0
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                visited.add(w)
                if w == endWord:
                    return minWords + 1
                for neighbor in graph[w]:
                    if neighbor in visited:
                        continue
                    q.append(neighbor)
            minWords += 1
        return 0
                

        

         
                    

