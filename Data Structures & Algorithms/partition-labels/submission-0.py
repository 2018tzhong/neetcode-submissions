from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # gather letters by their last index of appearance
        # also their first? then it would be an interval problem
        first = {}
        last = defaultdict(int)
        for idx, val in enumerate(s):
            last[val] = idx
            if not val in first:
                first[val] = idx

        intervals = []
        for key, val in first.items():
            # print(key, val)
            intervals.append([first[key], last[key]])
        
        intervals_sorted = sorted(intervals, key= lambda x: x[0])
        # print(intervals_sorted)
        ptr = 0
        merged = []
        for i in intervals_sorted:
            if len(merged) == 0:
                merged.append(i)
                continue
            curr_interval = merged.pop()
            # print("intervals", curr_interval, i)
            if i[0] < curr_interval[1]:
                merged.append([min(i[0], curr_interval[0]), max(i[1], curr_interval[1])])
            else:
                merged.append(curr_interval)
                merged.append(i)
            # print("curr merged", merged)
        # print("merged", merged)
        results = []
        curr_len = 0
        for i in merged:
            results.append(i[1]-curr_len+1)
            curr_len = i[1]+1
        return results



