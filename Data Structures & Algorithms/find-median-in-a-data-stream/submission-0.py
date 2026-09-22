class MedianFinder:

    def __init__(self):
        self.leftHalf = []
        self.rightHalf = []

    def addNum(self, num: int) -> None:
        if not self.leftHalf:
            self.leftHalf.append(num)
            return
        if num < self.leftHalf[0]:
            heapq.heappush_max(self.leftHalf, num)
        else:
            heapq.heappush(self.rightHalf, num)

        if abs(len(self.leftHalf) - len(self.rightHalf)) > 1:
            if len(self.leftHalf) > len(self.rightHalf):
                heapq.heappush(self.rightHalf, heapq.heappop_max(self.leftHalf))
            else:
                heapq.heappush_max(self.leftHalf, heap.heappop(self.rightHalf))

    def findMedian(self) -> float:
        if len(self.leftHalf) > len(self.rightHalf):
            return self.leftHalf[0]
        elif len(self.rightHalf) > len(self.leftHalf):
            return self.rightHalf[0]
        else:
            return (self.leftHalf[0] + self.rightHalf[0]) / 2
        
        