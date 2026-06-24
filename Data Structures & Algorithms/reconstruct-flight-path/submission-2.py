from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        sorted_tickets = sorted(tickets)
        # tickets_set = set([(i, j) for i, j in tickets])
        adj_map = defaultdict(list)
        for u, v in sorted_tickets:
            adj_map[u].append(v)
        # q = [("JFK", tickets_set.copy(), ["JFK"])]
        # while q:
        #     curr, s, path = q.pop()
        #     # print("checking", curr, s, path)
        #     if not s:
        #         return path
        #     for i in adj_map[curr]:
        #         if (curr, i) in s:
        #             new_s = s.copy()
        #             new_s.discard((curr, i))
        #             q.append((i, new_s, path + [i]))
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj_map:
                return False
            
            temp = list(adj_map[src])
            for idx, val in enumerate(temp):
                adj_map[src].pop(idx)
                res.append(val)
                if dfs(val): return True
                adj_map[src].insert(idx, val)
                res.pop()
            return False
        dfs("JFK")
        return res

