# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        if 1 <= n <= 2: return n
        cur_step, next_step = 1, 2
        for i in range(n-2):
            cur_step, next_step = next_step, cur_step + next_step
        return next_step