from collections import defaultdict
from sortedcontainers import SortedDict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # count them up
        # counts = defaultdict(int)
        counts = SortedDict()
        for val in hand:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1
        
        # print(counts)
        while len(counts.keys()) > 0:
            # print("iterating now for", counts.keys()[0])
            min_key = counts.keys()[0]
            for i in range(groupSize):
                if min_key not in counts:
                    return False
                counts[min_key] -= 1
                if counts[min_key] == 0:
                    counts.pop(min_key, None)
                min_key += 1

        return True
