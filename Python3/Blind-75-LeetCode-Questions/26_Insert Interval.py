# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START, END = 0, 1
        NEW_START, NEW_END = newInterval[0], newInterval[1]
        left, right = [], []
        for cur in intervals:
            #  check curInterval is on the left
            if cur[END] < NEW_START:
                left += [cur]
            #  check curInterval is on the right
            elif cur[START] > NEW_END:
                right += [cur]
            #  newInterval is mid of curInterval, so add min/max
            else:
                NEW_START = min(NEW_START, cur[START])
                NEW_END = max(NEW_END, cur[END])
        return left + [[NEW_START, NEW_END]] + right