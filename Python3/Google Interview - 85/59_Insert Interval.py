# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Complexity Analysis
# Time complexity : O(n)
# Space complexity : O(1)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START, END = 0, 1
        NEW_START, NEW_END = newInterval[0], newInterval[1]
        left, right = [], []
        for interval in intervals:
            #  check interval is on the left
            if interval[END] < NEW_START:
                left += [interval]
            #  check interval is on the right
            elif interval[START] > NEW_END:
                right += [interval]
            #  newInterval is mid of interval, so add min/max
            else:
                NEW_START = min(NEW_START, interval[START])
                NEW_END = max(NEW_END, interval[END])
        return left + [[NEW_START, NEW_END]] + right

# Create new List, but not fit to question request
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        
        result.append(newInterval); 
        return result