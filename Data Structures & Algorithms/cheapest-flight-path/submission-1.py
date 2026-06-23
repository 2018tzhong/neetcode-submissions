from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj_map = defaultdict(list)
        for s, d, price in flights:
            adj_map[s].append((price, d))
        
        q = [(0, src, 0, -1)]
        # visited = set()
        min_cost_so_far = math.inf
        while q:
            edge_cost, curr, total_cost, stops = heapq.heappop(q)
            if total_cost >= min_cost_so_far:
                continue
            if stops > k:
                continue
            if curr == dst:
                min_cost_so_far = min(total_cost, min_cost_so_far)
            for price_i, to_i in adj_map[curr]:
                heapq.heappush(q, (price_i, to_i, total_cost + price_i, stops + 1))
        if min_cost_so_far == math.inf:
            return -1
        return min_cost_so_far