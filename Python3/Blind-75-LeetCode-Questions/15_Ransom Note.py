# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in m and m[ransomNote[i]] != 0:
                m[ransomNote[i]] -= 1
            else:
                return False
        return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r, m = Counter(ransomNote), Counter(magazine)
        if r & m == r:
            return True
        else:
            return False