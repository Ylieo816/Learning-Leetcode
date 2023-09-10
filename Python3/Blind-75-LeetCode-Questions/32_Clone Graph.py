# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS - best solution
        if not node:    return node

        q, clone = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft()
            cur_clone = clone[cur.val]

            for neighbor in cur.neighbors:
                if neighbor.val not in clone:
                    clone[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)
                
                cur_clone.neighbors.append(clone[neighbor.val])
        return clone[node.val]

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        old_to_new = {}
        
        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy 
        
        return clone(node) if node else None