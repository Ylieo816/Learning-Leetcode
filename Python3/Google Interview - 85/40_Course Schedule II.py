# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 # Complexity Analysis
# - Time Complexity: O(V + E) where V is the number of vertices and E is the number edges.
# - Space Complexity: O(V + E) the adjacency list dominates our memory usage.
# # BFS with Kahn's algorithm for Topological Sorting
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]

        numPreq = [0] * numCourses

        record = [[] for _ in range(numCourses)]

        for course, preq in prerequisites:
            record[preq].append(course)
            numPreq[course] += 1

        q = deque()
        for i in range(numCourses):
            if numPreq[i] == 0:
                q.append(i)

        answer = []
        while q:
            cur = q.popleft()
            answer.append(cur)

            for next_course in record[cur]:
                numPreq[next_course] -= 1
                if numPreq[next_course] == 0:
                    q.append(next_course)
                    
        return answer if len(answer) == numCourses else []