class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = {}
        for task in tasks:      # O(m)
            if task in taskCount:
                taskCount[task] += 1
            else:
                taskCount[task] = 1
        nextTaskTracker = [(count, task) for task, count in taskCount.items()] # O(d), d is distinct tasks (d < m)
        heapq.heapify_max(nextTaskTracker) # O(d)
        nQueue = deque()
        result = 0
        while nextTaskTracker or nQueue:
            result += 1

            if nextTaskTracker:
                mostRemainingType = heapq.heappop_max(nextTaskTracker) # O(log(d))
                remainingCount = mostRemainingType[0]-1
                if remainingCount != 0:
                    mostRemainingType = (remainingCount, mostRemainingType[1])
                    nQueue.append((mostRemainingType, result+n))
            if nQueue:
                if nQueue[0][1] == result:
                    cooledDownTask = nQueue.popleft()
                    heapq.heappush_max(nextTaskTracker, cooledDownTask[0])  # O(log(d))

        return result

            