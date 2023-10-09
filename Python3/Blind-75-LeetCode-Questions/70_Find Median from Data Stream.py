# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

## Time COMPLEXITY : O(logN)
## Space COMPLEXITY : O(N)
class MedianFinder:

    def __init__(self):
        self.min_list = []  # store the largest value at the top
        self.max_list = [] # store the smallest value at the top

    def addNum(self, num: int) -> None:
        # heapq will store num by order from smallest to biggest
        # since heappop will pop the smallest, so add -1 to reverse order: 3,4,5 => -5, -4, -3
        if not self.max_list or num < -self.max_list[0]:
            heappush(self.max_list, -num)
        else:
            heappush(self.min_list, num)

        # balance size of heaps
        if len(self.min_list) + 1 < len(self.max_list):
            heappush(self.min_list, -heappop(self.max_list))
        elif len(self.min_list) > len(self.max_list):
            heappush(self.max_list, -heappop(self.min_list))

    def findMedian(self) -> float:
        # Time: O(1)
        if len(self.min_list) == len(self.max_list):
            return ( -self.max_list[0] + self.min_list[0] ) / 2.0

        return -self.max_list[0] / 1.0  


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()