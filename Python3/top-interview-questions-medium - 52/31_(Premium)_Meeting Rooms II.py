# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Heap
        """
        [[0,30],[5,10],[9,15],[15,18],[16,18],[19,20],[40,41] ]
        [0                                    30]
            [5  10]
               [9    15]
                     [15     18]
                         [16 18]
                                  [19 20] 
                                                   [40  41]
        [0,30],  h =[30]
        [5,10],  h =[10,30]
        [9,15],  h =[10,15,30]
        [15,18], h =[15,18,30]
        [16,18], h =[18,18,30]
        [19,20], h= [18,20,30]
		[40,41], h =[20,30,40]
        """
        heap = []
        intervals.sort()
        for interval in intervals:
            if not heap or heap[0] > interval[0]:
                # need a new meeting room
                heapq.heappush(heap, interval[1])
            else:
                # don't need a new meeting room, just update the end time
                heapq.heapreplace(heap, interval[1])

        return len(heap)