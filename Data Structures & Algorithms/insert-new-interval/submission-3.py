class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]        

        # do one pass 
        # check if intervals overlap with newInterval
        # can do this by checking if newInterval is before next one
        already_inserted = False
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0] and not already_inserted:
                intervals.insert(i, newInterval)
                already_inserted = True
        if not already_inserted:
            intervals.append(newInterval)

        # print(intervals)

        results = [intervals[0]]
        for i in range(1, len(intervals)):
            # print("running for ", i)
            # once we've added the new interval, we want to check with last interval
            last_interval = results.pop()
            if self.intervalsOverlap(last_interval, intervals[i]):
                new_interval = [min(last_interval[0], intervals[i][0]), max(last_interval[1], intervals[i][1])]
                results.append(new_interval)
            else:
                results.append(last_interval)
                results.append(intervals[i])
        return results
    
    def intervalsOverlap(self, i1, i2):
        return not (
            (i1[1] < i2[0]) or 
            (i1[0] > i2[1])
        )