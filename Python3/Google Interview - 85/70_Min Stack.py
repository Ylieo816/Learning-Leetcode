# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

c# Two list
# Time Complexity : O(1)
# Space Complexity : O(n)
# improvement: in push and pop, if smaller then push once, if [-1] == min_val: pop once
class MinStack:
    def __init__(self):
        self.stack, self.mini_num = [], []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini_num:
            self.mini_num.append(min(val, self.mini_num[-1]))
        else:
            self.mini_num.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mini_num.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini_num[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()