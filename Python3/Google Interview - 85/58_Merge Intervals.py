# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Complexity Analysis
# Time complexity : O(nlog⁡n)
# Space complexity : O(log⁡N) (or O(n)), the sorting itself takes O(log⁡n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        answer = []

        for interval in intervals:
            if not answer or answer[-1][1] < interval[0]:
                answer.append(interval)
            else:
                answer[-1][1] = max(answer[-1][1], interval[1])
        return answer