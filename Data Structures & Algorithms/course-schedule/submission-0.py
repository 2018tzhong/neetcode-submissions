from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # courses = set(range(numCourses))
        # print(courses)
        # starters = set(range(numCourses))
        prereqs = defaultdict(list)
        indegrees = defaultdict(int)
        for i, j in prerequisites:
            prereqs[j].append(i)
            indegrees[i] += 1
            # starters.discard(i)
        

        q = []
        for k in range(numCourses):
            if indegrees[k] == 0:
                q.append(k)
        # q = list(starters)
        # print(indegrees)
        visited = set()
        while q:
            curr = q.pop()
            visited.add(curr)
            if not curr in prereqs:
                continue
            for val in prereqs[curr]:
                indegrees[val] -= 1
                if indegrees[val] == 0:
                    q.append(val)
            # visited.add(curr)
        # print("check", visited)
        return len(visited) == numCourses
