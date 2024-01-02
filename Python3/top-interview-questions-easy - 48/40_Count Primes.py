# Given an integer n, return the number of prime numbers that are strictly less than n.

# use "Sieve of Eeatosthese" method: set True for all num(with it's times) before n^0.5
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                prime[i*i:n:i] = [False] * len(prime[i*i:n:i])
        return sum(prime)