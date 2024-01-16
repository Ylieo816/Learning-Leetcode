# Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

# All messages will come in chronological order. Several messages may arrive at the same timestamp.

# Implement the Logger class:

# - Logger() Initializes the logger object.
# - bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.

# Time Complexity: O(1)
# Space Complexity: O(M), M is the size of all incoming messages
class Logger:

    def __init__(self):
        self.table = {}        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.table:
            if timestamp - self.table[message] >= 10:
                self.table[message] = timestamp
                return True
        else:
            self.table[message] = timestamp
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)