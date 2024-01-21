# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Doubly Linked List
# Time complexity: O(1) for both get and put
# Space complexity: O(capacity)
class LRUCache:
    class Node:
       # use bi-directional Node to save trace
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.pre = None
            self.next = None

    def __init__(self, capacity: int):
        # save capa, set head and tail and link together, table to save cur value
        self.capacity = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.table = {}

    def addNodeToHead(self, Node):
        # insert node to head
        tmp = self.head.next
        Node.next = tmp
        Node.pre = self.head
        self.head.next = Node
        tmp.pre = Node
    
    def deleteNode(self, node):
        # delete specific node
        prev = node.pre
        nextt = node.next
        prev.next = nextt
        nextt.pre = prev

    def get(self, key: int) -> int:
        # if exist, extract key-value and del in table and node, and add it again
        if key in self.table:
            node = self.table[key]
            answer = node.val
            del self.table[key]
            self.deleteNode(node)
            self.addNodeToHead(node)
            self.table[key] = self.head.next
            return answer
        return -1

    def put(self, key: int, value: int) -> None:
        # if exist, remove it and add node again
        if key in self.table:
            node = self.table[key]
            del self.table[key]
            self.deleteNode(node)
        
        # if more than capacity, delete the last one since it's priority is lowest
        if len(self.table) == self.capacity:
            del self.table[self.tail.pre.key]
            self.deleteNode(self.tail.pre)

        self.addNodeToHead(self.Node(key, value))
        self.table[key] = self.head.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# OrderedDict with move_to_end
# Time complexity: O(1) for both get and put
# Space complexity: O(capacity)
import collections
class LRUCache:
    def __init__(self, capacity: int):
        self.table = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1

        self.table.move_to_end(key)
        return self.table[key]

    def put(self, key: int, value: int) -> None:
        self.table[key] = value
        self.table.move_to_end(key)
        if len(self.table) > self.capacity:
            self.table.popitem(last = False) # delete first key-value