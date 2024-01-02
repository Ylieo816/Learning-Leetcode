# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Heap
# Complexity Analysis
# Time Complexity: O(NlogK)
# Space Complexity: O(K), K is heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heapq is a heap queue which will rank inputed data from smail to big
        heap = []
        for (x, y) in points:
            #  since heapq pop will pop the smallest root, so we reverse the squrt value
            sq = -(x*x + y*y)
            if len(heap) < k:
                heapq.heappush(heap, (sq, x, y))
            else:
                # heappushpop will push a value and pop the smaillest root
                heapq.heappushpop(heap, (sq, x, y))
        return [(x, y) for (d, x, y) in heap]


# Complexity Analysis
# Time Complexity: O(Nlog⁡N)
# Space Complexity: O(N)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # math method
        distance = []
        answer = []

        for i in range(len(points)):
            d = ((points[i][0] ** 2)+(points[i][1] ** 2)) ** 0.5
            distance.append([d, points[i]])
        
        distance.sort()

        for i in range(k):
            answer.append(distance[i][1])
        return answer