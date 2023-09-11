# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Complexity Analysis
# - Time Complexity: O(V + E) where V is the number of vertices and E is the number edges.
# - Space Complexity: O(V + E) the adjacency list dominates our memory usage.
# # BFS with Kahn's algorithm for Topological Sorting
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #  numPreq: how many preq-courses do this course has
        numPreq = [0] * numCourses
        #  the course is what courses' preq
        record = [[] for _ in range(numCourses)]
        
        # save each preq-course includs courses && how many time be used for each course
        for pair in prerequisites:
            course, preq = pair[0], pair[1]
            record[preq].append(course)
            numPreq[course] += 1

        # start running for the course which is not used
        q = deque()
        for i in range(numCourses):
            if numPreq[i] == 0:
                q.append(i)

        # each course should be run at least once
        answer = []
        while q:
            cur = q.popleft()
            answer.append(cur)

            for next_course in record[cur]:
                numPreq[next_course] -= 1
                # if all pre are reached, run this course next time
                if numPreq[next_course] == 0:
                    q.append(next_course)
        
        return len(answer) == numCourses