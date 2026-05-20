"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        prev_end = 0
        for i in sorted_intervals:
            if i.start < prev_end:
                return False
            else:
                prev_end = i.end
        return True

    def intervalsOverlap(self, i1, i2):
        return not (
            (i1.start > i2.end) or
            (i1.end < i2.start)
        )