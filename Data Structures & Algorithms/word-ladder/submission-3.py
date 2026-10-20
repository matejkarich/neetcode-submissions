class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        minWords = 1
        q = deque()
        q.append(beginWord)
        visited = set()

        def generateNeighbors(w):
            for i in range(len(w)):
                for j in range(ord('a'), ord('z')+1):
                    if w[i] == chr(j):
                        continue
                    newWord = w[:i] + chr(j) + w[i+1:]
                    if newWord in wordSet:
                        q.append(newWord)
                        visited.add(newWord)

        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return minWords
                generateNeighbors(w)
            minWords += 1

        return 0