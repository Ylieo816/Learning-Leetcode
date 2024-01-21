# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

# One pass
# Optimized check three conditions
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        L_count, R_count = 0, 0
        for i in range(len(start)):
            if start[i] == 'L':
                L_count += 1
            if end[i] == 'L':
                L_count -= 1
            if L_count > 0:
                return False

            if start[i] == 'R':
                R_count += 1
            if end[i] == 'R':
                R_count -= 1
            if R_count < 0:
                return False
        return L_count == 0 and R_count == 0

# check len same
# check RL order same because order change is only for X with R/L
# check the order is right for L (end idx <= start) and R (end idx >= start)
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        Lstart, Lend, Rstart, Rend = [], [], [], []
        for i in range(len(start)):
            if start[i] == 'L':
                Lstart.append(i)
            if start[i] == 'R':
                Rstart.append(i)

        for i in range(len(end)):
            if end[i] == 'L':
                Lend.append(i)
            if end[i] == 'R':
                Rend.append(i)
        
        for i, j in zip(Lstart, Lend):
            if j > i:
                return False

        for i, j in zip(Rstart, Rend):
            if i > j:
                return False
        return True