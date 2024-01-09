# Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Backtracking Algorithm

# # Recursion
# # Complexity Analysis
# # Time complexity: N⋅5 ^(⌊N/2⌋+1)
# # Space complexity: N⋅5 ^(⌊N/2⌋+1)
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        table = [
            ['0', '0'], ['1', '1'],
            ['6', '9'], ['8', '8'], ['9', '6']
        ]

        def generate_num(n, total_len):
            # no middle
            if n == 0:
                return ['']
            
            # for odd , the middle will consist of ['0', '1', '8']
            if n == 1:
                return ['0', '1', '8']
            
            # for even, divide to the middle of smaller and consist of two middle
            middle_stro = generate_num(n - 2, total_len)
            cur_stro = []

            for stro in middle_stro:
                for pair in table:
                    # can't append '0' at the beginning
                    if pair[0] != '0' or n != total_len:
                        cur_stro.append(pair[0] + stro + pair[1])
            return cur_stro

        return generate_num(n, n)

# Loop
# Complexity Analysis
# Time complexity: N⋅5 ^(⌊N/2⌋+1)
# Space complexity: N⋅5 ^(⌊N/2⌋+1)
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        table = [
            ['0', '0'], ['1', '1'],
            ['6', '9'], ['8', '8'], ['9', '6']
        ]

        # When n is even (n % 2 == 0), we start with strings of length 0 and
        # when n is odd (n % 2 == 1), we start with strings of length 1.
        total_len = n % 2

        q = ["0", "1", "8"] if total_len == 1 else [""]
        while total_len < n:
            total_len += 2
            next_level = []

            for num in q:
                for pair in table:
                    if pair[0] != '0' or n != total_len:
                        next_level.append(pair[0] + num + pair[1])
                q = next_level
        return q