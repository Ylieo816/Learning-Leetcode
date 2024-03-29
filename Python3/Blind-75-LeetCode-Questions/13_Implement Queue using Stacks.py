# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

class MyQueue:

    def __init__(self):
        self.in_stack = [] # for input data
        self.out_stack = [] # for output data
        # Push element x to the back of queue...

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x) # input data to the stack

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek() # move data from input data to output data
        return self.out_stack.pop() # return first element from the input data

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.out_stack:
            while self.in_stack: # move all elements from input stack to output stack
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1] # return the last element

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.out_stack and not self.in_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()