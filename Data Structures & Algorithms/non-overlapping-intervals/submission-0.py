class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        # keep a count of max intervals overlapping

        # keep track of which ones overlap with each other

        # in terms of count

        # subtract using max intersections until all 

        # could I use a union find?

        prevEnd = -50000
        removals = 0
        for i in range(len(sorted_intervals)):
            if sorted_intervals[i][0] < prevEnd:
                # intersects
                removals += 1
                prevEnd = min(prevEnd, sorted_intervals[i][1])
            else:
                prevEnd = sorted_intervals[i][1]
        return removals
