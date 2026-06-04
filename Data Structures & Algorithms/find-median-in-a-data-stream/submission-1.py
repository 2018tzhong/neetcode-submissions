class MedianFinder:

    def __init__(self):
        self.top = [] # min heap
        self.bottom = [] # max heap

    def addNum(self, num: int) -> None:

        if len(self.top) == 0:
            heapq.heappush(self.top, num)
        elif num < self.top[0]:
            heapq.heappush(self.bottom, -num)
        else:
            # add to top
            heapq.heappush(self.top, num)
        
        if len(self.top) >= len(self.bottom) + 2:
            val = -heapq.heappop(self.top)
            heapq.heappush(self.bottom, val)
        if len(self.bottom) >= len(self.top) + 2:
            val = -heapq.heappop(self.bottom)
            heapq.heappush(self.top, val)

    def findMedian(self) -> float:
        if len(self.top) == 0 and len(self.bottom) == 0:
            return None
        if len(self.top) == len(self.bottom):
            topval = self.top[0]
            bottomval = -self.bottom[0]
            return (topval + bottomval)/ 2.0
        elif len(self.top) > len(self.bottom):
            return self.top[0]
        else:
            return -self.bottom[0]