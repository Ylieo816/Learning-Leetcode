# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# - The number of "bulls", which are digits in the guess that are in the correct position.
# - The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

# Optimized One pass
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        diff_dict = defaultdict(int)
        bulls = cows = 0

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                if diff_dict[g] < 0:
                    cows += 1
                diff_dict[g] += 1

                if diff_dict[s] > 0:
                    cows += 1
                diff_dict[s] -= 1

        return str(bulls) + 'A' + str(cows) + 'B'

# One pass answer
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        table_secret, table_guess = defaultdict(int), defaultdict(int)
        A, B = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if (secret[i] in table_guess) and (table_guess[secret[i]] > 0):
                    B += 1
                    table_guess[secret[i]] -= 1
                else:
                    table_secret[secret[i]] += 1
                
                if (guess[i] in table_secret) and (table_secret[guess[i]] > 0):
                    B += 1
                    table_secret[guess[i]] -= 1
                else:
                    table_guess[guess[i]] += 1
        return str(A) + 'A' + str(B) + 'B'