"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        elif len(intervals) == 1:
            return 1

        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        

        min_rooms = 1
        stack = []
        for i in range(len(sorted_intervals)):
            # pop off from stack if they don't intersect
            while stack and not sorted_intervals[i].start < stack[0]:
                heapq.heappop(stack)

            heapq.heappush(stack, sorted_intervals[i].end)
            # print("for ", i, stack)
            min_rooms = max(min_rooms, len(stack))
        return min_rooms