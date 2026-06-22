from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereqs = defaultdict(list)
        indegrees = defaultdict(int)
        for i, j in prerequisites:
            indegrees[i] += 1
            prereqs[j].append(i)
        
        q = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        order = []
        visited = set()
        while q:
            curr = q.pop(0)
            if curr in visited:
                continue
            visited.add(curr)
            order.append(curr)
            for v in prereqs[curr]:
                indegrees[v]-= 1
                if indegrees[v] == 0:
                    q.append(v)
        if len(visited) == numCourses:
            return order
        return []