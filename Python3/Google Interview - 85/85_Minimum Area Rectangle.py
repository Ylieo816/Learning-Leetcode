# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

# Time complexity: O(N^2)
# Space complexity: O(N)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        points_set = set()
        for point in points:
            points_set.add(tuple(point))
        
        mini_area = float('inf')
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i+1:]):
                if (x1 < x2 and y1 < y2 
                    and (x1, y2) in points_set and (x2, y1) in points_set):
                    area = (x2 - x1) * (y2 - y1)
                    mini_area = min(mini_area, area)
        return mini_area if mini_area != float('inf') else 0
    
# Bruce solution
# Time complexity: O(N^2)
# Space complexity: O(N)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_seen = set()        
        mini_area = float('inf')
        for (x1, y1) in (points):
            for (x2, y2) in (points):
                if ((x1, y2) in points_seen and (x2, y1) in points_seen):
                    area = abs((x2 - x1) * (y2 - y1))
                    mini_area = min(mini_area, area)
            points_seen.add((x1, y1))
        return mini_area if mini_area != float('inf') else 0