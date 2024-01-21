# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

# A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

# Implement the MyCalendarTwo class:

# - MyCalendarTwo() Initializes the calendar object.
# - boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

class MyCalendarTwo:

    def __init__(self):
        self.single_booked = []
        self.double_booked = []

    def book(self, start: int, end: int) -> bool:
        # first check for a overlap interval in double booked
        for s, e in self.double_booked:
            if start < e and end > s:
                return False
        
        for s, e in self.single_booked:
            if start < e and end > s:
                self.double_booked.append((max(start, s), min(end, e)))
        self.single_booked.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)