# Android devices have a special lock screen with a 3 x 3 grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of k dots is a valid unlock pattern if both of the following are true:

# All the dots in the sequence are distinct.
# If the line segment connecting two consecutive dots in the sequence passes through the center of any other dot, the other dot must have previously appeared in the sequence. No jumps through the center non-selected dots are allowed.
# For example, connecting dots 2 and 9 without dots 5 or 6 appearing beforehand is valid because the line from dot 2 to dot 9 does not pass through the center of either dot 5 or 6.
# However, connecting dots 1 and 3 without dot 2 appearing beforehand is invalid because the line from dot 1 to dot 3 passes through the center of dot 2.
# Here are some example valid and invalid unlock patterns:

# - The 1st pattern [4,1,3,6] is invalid because the line connecting dots 1 and 3 pass through dot 2, but dot 2 did not previously appear in the sequence.
# - The 2nd pattern [4,1,9,2] is invalid because the line connecting dots 1 and 9 pass through dot 5, but dot 5 did not previously appear in the sequence.
# - The 3rd pattern [2,4,1,3,6] is valid because it follows the conditions. The line connecting dots 1 and 3 meets the condition because dot 2 previously appeared in the sequence.
# - The 4th pattern [6,5,4,1,9,2] is valid because it follows the conditions. The line connecting dots 1 and 9 meets the condition because dot 5 previously appeared in the sequence.
# Given two integers m and n, return the number of unique and valid unlock patterns of the Android grid lock screen that consist of at least m keys and at most n keys.

# Two unlock patterns are considered unique if there is a dot in one sequence that is not in the other, or the order of the dots is different.

# Backtracking
# Similar to 46.Permutations (排列)
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        invalid = {
            (1, 3): 2, (3, 1): 2,
            (1, 7): 4, (7, 1): 4, 
            (1, 9): 5, (9, 1): 5, (2, 8): 5,(8, 2): 5,
            (3, 7): 5, (7, 3): 5, (4, 6): 5,(6, 4): 5,
            (3, 9): 6, (9, 3): 6, 
            (7, 9): 8, (9, 7): 8 
        }
        answer = 0
        visited = [0] * 10

        def backtracking(cur, path, visited):
            nonlocal answer
            if len(path) == n:
                return
            for i in range(1, 10):
                if (not visited[i] and
                    (((cur, i) not in invalid) or visited[invalid[(cur, i)]])):
                    path.append(i)
                    visited[i] = 1
                    backtracking(i, path, visited)

                    if len(path) >= m:
                        answer += 1
                    path.pop(-1)
                    visited[i] = 0
        
        backtracking(None, [], visited)
        return answer