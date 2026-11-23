class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort()
        adjList = {}
        for start, dest in tickets:
            if start not in adjList:
                adjList[start] = []
            adjList[start].append(dest)

        stack = ["JFK"]
        result = []
        while stack:
            currentAirport = stack[-1]
            if currentAirport not in adjList or not adjList[currentAirport]:
                result.append(stack.pop())
            else:
                stack.append(adjList[currentAirport].pop(0))

        print(result)
        return result[::-1]
        