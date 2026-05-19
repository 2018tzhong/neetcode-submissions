class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        sorted_intervals = sorted(intervals,key=lambda x: x[0])

        # print(sorted_intervals)
        results = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            last_interval = results.pop()
            # print("check overlap", self.intervalOverlap(last_interval, sorted_intervals[i]))
            if self.intervalOverlap(last_interval, sorted_intervals[i]):
                new_interval = [min(last_interval[0], sorted_intervals[i][0]), max(last_interval[1], sorted_intervals[i][1])]
                results.append(new_interval)
            else:
                results.append(last_interval)
                results.append(sorted_intervals[i])
        return results


    def intervalOverlap(self, i1, i2):
        return not (
            (i1[1] < i2[0]) or 
            (i1[0] > i2[1])
        )