# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.

# - Add every overlapped intervals to heap
# - If there is no overlap intervals then pop the element and find profit till that point
# - Repeat this to find max-profit till last

# Time complexity: O(n log n)
# Space complexity: O(n)

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs = sorted(jobs)
        cur_pro, max_pro = 0, 0
        heap = []
        for st, et, pro in jobs:
            while heap and heap[0][0] <= st:
                e, p = heappop(heap)
                cur_pro = max(cur_pro, p)
            heappush(heap, (et, cur_pro + pro))
            max_pro = max(max_pro, cur_pro + pro)
        return max_pro