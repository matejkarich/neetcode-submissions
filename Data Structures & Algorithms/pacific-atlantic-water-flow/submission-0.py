class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        pacific = set()
        atlantic = set()
        result = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    q.append((r,c, "P"))
                if r == len(heights)-1 or c == len(heights[0])-1:
                    q.append((r,c, "A"))
        print(q)
        while q:
            block = q.popleft()
            x,y,ocean = block[0], block[1], block[2]
            directions = [(x-1,y,ocean),(x+1,y,ocean),(x,y-1,ocean),(x,y+1,ocean)]
            for d in directions:
                r,c = d[0], d[1]
                if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]) or d in visited or heights[r][c] < heights[x][y]:
                    continue
                q.append(d)
                visited.add(d)
            if ocean == "P":
                pacific.add((x,y))
            else:
                atlantic.add((x,y))

        for pair in pacific:
            if pair in atlantic:
                result.append([pair[0],pair[1]])
        return result
