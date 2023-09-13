# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# - MinStack() initializes the stack object.
# - void push(int val) pushes the element val onto the stack.
# - void pop() removes the element on the top of the stack.
# - int top() gets the top element of the stack.
# - int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
        

#     def pop(self) -> None:
#         self.stack.pop()
        

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return min(self.stack)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mini_num = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.mini_num:
            self.mini_num.append(min(self.mini_num[-1], x))
        else:
            self.mini_num.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.mini_num.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini_num[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()