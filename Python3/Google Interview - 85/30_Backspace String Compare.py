# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Build String
# Time Complexity: O(M+N)
# Space Complexity: O(M+N)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stack_process(st):
            stack = []
            for i in range(len(st)):
                if st[i] != '#':
                    stack.append(st[i])
                elif st[i] == '#' and stack:
                    stack.pop()

            return ''.join(stack)

        return stack_process(s) == stack_process(t)