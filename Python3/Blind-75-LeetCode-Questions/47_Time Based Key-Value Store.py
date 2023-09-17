# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# - TimeMap() Initializes the object of the data structure.
# - void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# - String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = ['']
        self.table[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        # # originally, we should serach the closet answer
        # answer = ''
        # # find key's list, or returns empty list [values is a list]
        # value = self.table.get(key, [])

        # # Binary Search
        # left, right = 0, len(value) - 1
        
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if value[mid][1] <= timestamp:
        #         answer = value[mid][0]  # the closet answer, it should smaller or equal to the timestamp
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return answer

        # But timestamp is always in increasing order, 
        # we can just search from the last element of array and return after edge cases.
        if key not in self.table:
            return ''

        for i in range(len(self.table[key]) - 1, -1, -1):
            if self.table[key][i] == '':
                return ''
            v, t = self.table[key][i]
            if t <= timestamp:
                return v


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)