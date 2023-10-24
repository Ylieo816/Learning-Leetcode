# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Best answre
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        q = deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)):
                cur = q.popleft()
                cur.next, rightNode = rightNode, cur
                if cur.right:
                    q.extend([cur.right, cur.left])
        return root

# BFS, slower
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = deque()
        q.append((root, 0))
        while q:
            node, level = q.popleft()

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

            if not q or level != q[0][1]:
                node.next = None
            else:
                node.next = q[0][0]
        return root