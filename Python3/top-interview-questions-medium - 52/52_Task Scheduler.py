# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.

# Time complex: O(n) 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table = Counter(tasks)
        max_len = max(table.values())
        # List the max num of Char to block
        # e.g. ACCCEEE 2 ==> CE_CE_CE => (max num - 1) * (n + 1) + max num
        count = (max_len - 1) * (n + 1)
        for cnt in table.values():
            if cnt == max_len:
                count += 1
        return max(count, len(tasks))