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
        nQueue = []
        result = []
        while nextTaskTracker or nQueue:
            if nextTaskTracker:
                mostRemainingType = heapq.heappop_max(nextTaskTracker) # O(log(d))
                result.append(mostRemainingType[1])
                remainingCount = mostRemainingType[0]-1
                if remainingCount == 0:
                    nQueue.append(None)
                else:
                    mostRemainingType = (remainingCount, mostRemainingType[1])
                    nQueue.append(mostRemainingType)
            else:
                if all(item is None for item in nQueue):
                    break
                result.append("_")
                nQueue.append(None)

            if len(nQueue) == (n + 1):
                cooledDownTask = nQueue.pop(0)
                if cooledDownTask is not None:
                    heapq.heappush_max(nextTaskTracker, cooledDownTask)  # O(log(d))
            # print(result)
            # print(nQueue)
            # print(nextTaskTracker)
        return len(result)

            
