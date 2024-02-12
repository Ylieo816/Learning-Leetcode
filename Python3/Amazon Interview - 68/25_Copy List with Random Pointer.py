# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Recursion with Hash Map
# Complexity Analysis
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def __init__(self):
        # key: old node
        # value: new node
        self.visited = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # if the node already process, run cloned node
        if head in self.visited:
            return self.visited[head]

        # new clone node
        node = Node(head.val, None, None)

        # save clone to dict
        self.visited[head] = node

        # Recursive copy next and random node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

# Loop with Hash Map
# Complexity Analysis
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        visited = {}

        cur = head
        while cur:
            visited[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            visited[cur].next = visited.get(cur.next)
            visited[cur].random = visited.get(cur.random)
            cur = cur.next
        
        return visited[head]

# Loop with Interweaving Nodes
# Complexity Analysis
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        while cur:
            # Origin: A -> B
            # After: A -> A' -> B -> B'
            new_node = Node(cur.val, cur.next)
            cur.next = new_node
            cur = new_node.next
        
        cur = head
        while cur:
            # check cur has random
            # if so, A' random -> A random
            # A' random: cur.next.random
            # A random: cur.random.next
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # seperate old node and new node
        old_head, new_head = head, head.next
        cur_old, cur_new = old_head, new_head

        while cur_old:
            cur_old.next = cur_old.next.next
            cur_new.next = cur_new.next.next if cur_new.next else None
            cur_old = cur_old.next
            cur_new = cur_new.next

        return new_head