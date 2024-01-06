# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

# Path Search in Graph
# Complexity Analysis:
# Time Complexity: O(M⋅N), N: iterate equations build a graph, M: query size
# Space Complexity: O(N): build a graph
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # dfs to traverse all nextDist until found the distination
        def dfs(ori, dst, gra, visited, ans, tmp):
            if ori in visited:
                return
            
            visited.add(ori)
            if ori == dst:
                ans[0] = tmp
                return
            
            for neighbor, val in gra[ori].items():
                dfs(neighbor, dst, gra, visited, ans, tmp * val)

        def buildGraph(equations, values):
            gra = {}

            for i in range(len(equations)):
                dividend, divisor = equations[i]
                value = values[i]

                if dividend not in gra:
                    gra[dividend] = {}
                if divisor not in gra:
                    gra[divisor] = {}
                
                gra[dividend][divisor] = value
                gra[divisor][dividend] = 1.0 / value
            
            return gra
        
        graphTable = buildGraph(equations, values)
        answer = []

        for query in queries:
            dividend, divisor = query

            if dividend not in graphTable or divisor not in graphTable:
                answer.append(-1.0)
            else:
                ans = [-1.0]
                dfs(dividend, divisor, graphTable, set(), ans, 1.0)
                answer.append(ans[0])

        return answer