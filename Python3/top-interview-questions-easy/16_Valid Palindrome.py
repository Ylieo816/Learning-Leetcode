# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        data = ""
        for i in range(len(s)):
            if "0" <= s[i] <= "9" or "a" <= s[i] <= "z":
                data += s[i]
        return data == data[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1, ptr2 = 0, len(s) -1
        s = s.lower()
        while(ptr1 < ptr2):
            if not (("0" <= s[ptr1] <= "9") or ("a" <= s[ptr1] <= "z")):
                ptr1 += 1
            elif not (("0" <= s[ptr2] <= "9") or ("a" <= s[ptr2] <= "z")):
                ptr2 -= 1
            else:
                if s[ptr1] != s[ptr2]:
                    return False
                ptr1 += 1
                ptr2 -= 1
        return True