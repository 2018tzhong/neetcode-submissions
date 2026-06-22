from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        indegrees = defaultdict(int)
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
            indegrees[j] += 1
        
        q = [(0, -1)]
        visited = set()
        while q:
            curr, parent = q.pop(0)
            if curr in visited:
                return False
            
            visited.add(curr)
            for v in adj[curr]:
                if v == parent:
                    continue
                q.append((v, curr))
        return len(visited) == n
        # print(visited)
        # if len(visited) == n:
            # return True
        # return False