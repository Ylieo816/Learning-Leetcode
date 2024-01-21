# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

# Union-find
class Solution:
    def removeStones(self, stones):
        UF = {}
        
        ### Given an element, find the root of the group to which this element belongs.
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            ### this may be the first time we see x or y, so set itself as the root.
            if x not in UF:
                UF[x] = x
            if y not in UF:
                UF[y] = y
            rootX = find(x)
            rootY = find(y)
            # set the root of y (rootY) as the root of the root of x (rootX)
            UF[rootX] = rootY
        
        ### Since x and y can be the same, but 0 <= x, y <= 10^4, we can add 10^4 to every y 
        maxX = 10**4+1
        for x,y in stones:
            union(x,y+maxX)
        
        return len(stones) - len({find(n) for n in UF})

# # DFS
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        length = len(stones)
        row, col = defaultdict(list), defaultdict(list)

        def DFS(xo,yo):
            nonlocal visited
            if (xo,yo) not in visited:
                visited.add((xo,yo))
                for neiY in row[xo]:
                    DFS(xo,neiY)
                for neiX in col[yo]:
                    DFS(neiX,yo)
        
        answer = []
        connectedComponent = 0
        # link all neighbors
        for x, y in stones:
            row[x].append(y)
            col[y].append(x)

        # check all points
        visited = set()
        for x, y in stones:
            if (x, y) not in visited:
                DFS(x, y)
                connectedComponent += 1

        return len(stones) - connectedComponent

# # BFS
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        ### construct graph
        ### Uing two hash map to store the neighbors on the x-axis and y-axis 
        graphX = defaultdict(list)
        graphY = defaultdict(list)
        for x,y in stones:
            graphX[x].append(y)
            graphY[y].append(x)
        
        ### For each stone, if we haven't seen it before, use a BFS to find all stones connects to it
        ### For each connected component, there will always be 1 stone that can not be removed
        ### so once we know the number of connected component, 
        ### we can subtract it from totoal number of stones to find the number of removed stones
        connectedComponent = 0
        ### each stone should only be visited once.
        visited = set()
        for x,y in stones:
            ### if the current stone has not been visited, do a BFS from it.
            if (x,y) not in visited:
                q = deque([(x,y)])
                while q:
                    xo,yo = q.popleft()
                    ### check to see if the current stone has been visited, 
                    ### if not, get its neighbors
                    if (xo,yo) not in visited:
                        visited.add((xo,yo))
                        ### since we used two hash map to store the neighbors,
                        ### we need to get all the neighbors fron the current stone.
                        for neiY in graphX[xo]:
                            q.append((xo,neiY))
                        for neiX in graphY[yo]:
                            q.append((neiX,yo))
                ### we find another connected component
                connectedComponent += 1
        
        return len(stones)-connectedComponent