from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # mst
        # kruskals?
        sorted_edges = sorted(times, key=lambda x: x[2])
        adj_map = defaultdict(list)
        for u, v, t in sorted_edges:
            adj_map[u].append((t, v))
        
        q = adj_map[k]
        heapq.heapify(q)
        mst = 0
        visited = set({k})
        # print("starting", q)
        while q:
            # print("checking", q)
            cost, curr = heapq.heappop(q)
            # print(cost, curr)
            if len(visited) == n:
                break
            if curr in visited:
                continue
            visited.add(curr)
            mst = max(cost, mst)
            for t, v in adj_map[curr]:
                heapq.heappush(q, (cost + t, v))

        # print(visited, len(visited))
        if len(visited) == n:
            return mst
        return -1