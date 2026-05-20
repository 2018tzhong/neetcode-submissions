import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-i for i in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            print("stones", neg_stones)
            # do stuff
            s1 = heapq.heappop(neg_stones)
            s2 = heapq.heappop(neg_stones)
            diff = abs(s1 - s2)
            if diff != 0:
                heapq.heappush(neg_stones, -diff)

        return -neg_stones[0] if len(neg_stones) == 1 else 0