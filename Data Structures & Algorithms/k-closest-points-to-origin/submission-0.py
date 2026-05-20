import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for i in points:
            heapq.heappush(heap, (self.dist(i), i))
        kmin = heapq.nsmallest(k, heap)
        return [i[1] for i in kmin]

    def dist(self, p):
        return math.sqrt(p[0] ** 2 + p[1] ** 2)