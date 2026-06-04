import heapq
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = defaultdict(int)
        for i in tasks:
            m[i] += 1
        
        h = []
        for k, v in m.items():
            heapq.heappush(h, (-v, k))

        cooldown = [None for i in range(n)]
        counter = 0
        while h:
            curr = heapq.heappop(h)
            if -curr[0] - 1 > 0:
                cooldown.append((curr[0]+1, curr[1]))
            else:
                cooldown.append(None)
            cooldown_val = cooldown.pop(0)
            if cooldown_val != None:
                heapq.heappush(h, cooldown_val)
            counter += 1
        # print("counter after looping", counter, cooldown)
        # now how do we handle ending?
        # edge case where cooldown queue is still filled after h empties
        max_val_remaining = 0
        cooldown_remaining = 0
        do_flag = False
        for i in range(len(cooldown)):
            curr_node = cooldown[i]
            if curr_node and -curr_node[0] >= max_val_remaining:
                do_flag = True
                max_val_remaining = -curr_node[0]
                cooldown_remaining = i + 1
        if do_flag:
            counter = counter + cooldown_remaining + 1 + (n+1) * (max_val_remaining - 1)
        return counter