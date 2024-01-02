# Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.

# Implement the Vector2D class:

# Vector2D(int[][] vec) initializes the object with the 2D vector vec.
# next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
# hasNext() returns true if there are still some elements in the vector, and false otherwise.

class Vector2D:
# Time Complexity: O(1)
# Space Complexity: O(v.size)
    def __init__(self, vec: List[List[int]]):
        self.ptr = -1
        self.table = []
        for i in range(len(vec)):
            self.table = self.table + vec[i]

    def next(self) -> int:
        self.ptr += 1
        return self.table[self.ptr]

    def hasNext(self) -> bool:
        if (self.ptr+1)  >= len(self.table):
            return False
        else:
            return True

class Vector2D:
# Time Complexity: O(1)
# Space Complexity: O(1)
    def __init__(self, v: List[List[int]]):
        self.table = v
        self.col = 0
        self.row = 0

    def next(self) -> int:
        self.hasNext()
        val = self.table[self.row][self.col]
        self.col += 1
        return val

    def hasNext(self) -> bool:
        while self.row < len(self.table):
            if self.col < len(self.table[self.row]):
                return True
            self.row += 1
            self.col = 0
        return False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()