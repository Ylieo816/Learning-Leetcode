# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

class Solution:
    def nextClosestTime(self, time: str) -> str:
        HH, MM = time.split(':')

        # sort all digits
        nums = sorted(set(HH+MM))

        # Generate all possible 2 digit values, a total of 16 kinds
        two_digits = []
        for first in nums:
            for second in nums:
                two_digits.append(first + second)

        # find current MM idx
        mm_idx = two_digits.index(MM)
        # if cur MM has next, return next
        if mm_idx + 1 < len(two_digits) and two_digits[mm_idx+1] < '60':
            return HH + ':' + two_digits[mm_idx+1]

        # MM has carry to HH, so check HH
        # find current HH idx
        hh_idx = two_digits.index(HH)
        # if cur HH has next, return next
        if hh_idx + 1 < len(two_digits) and two_digits[hh_idx+1] < '24':
            return two_digits[hh_idx+1] + ':' + two_digits[0]

        # HH and MM have carry, so return origin
        return two_digits[0] + ':' + two_digits[0]

# Count until match existed value
class Solution:
    def nextClosestTime(self, time: str) -> str:
        h, m = map(int, time.split(':'))

        digits = {h%10, h//10, m%10, m//10}

        while True:
            m += 1
            if m == 60:
                h += 1
                m = 0

                if h == 24:
                    h = 0
            if all([digit in digits for digit in [h%10, h//10, m%10, m//10]]):
                return f'{h:02}:{m:02}'