# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.end)

        tail = intervals[0].end
        count = 1
        for i in intervals:
            if i.start >= tail:
                count += 1
                tail = i.end
        return len(intervals) - count            

