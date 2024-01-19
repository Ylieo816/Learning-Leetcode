# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = set(jewels)
        answer = 0
        for stone in (stones):
            if stone in table:
                answer += 1
        return answer

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew_list = list(jewels)
        answer = 0
        for jewel in jew_list:
            answer += stones.count(jewel)
        return answer