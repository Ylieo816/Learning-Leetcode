# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to the closest person.

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        lengthOfSeat = len(seats)
        
        # find most left side
        left = 0
        while left < lengthOfSeat and seats[left] == 0:
            left += 1

        # find most right side
        right = lengthOfSeat - 1
        while right > 0 and seats[right] == 0:
            right -= 1

        # find the middle part
        cnt = 0
        interval = 0
        for i in range(left + 1, right + 1, 1):
            if seats[i] == 0:
                cnt += 1
            else:
                interval = max(interval, cnt)
                cnt = 0

        return max(left, lengthOfSeat - right - 1, (interval+1) // 2 )

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, dist = 0, seats.index(1)
        
        for seat in seats:
            if seat: 
                res, dist = max(res, math.ceil(dist/2)), 0
            else: 
                dist += 1
                
        return max(res, dist)