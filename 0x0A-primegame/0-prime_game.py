#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """
    Determines the winner based on the given list of numbers.

    Args:
        x (int): An integer representing the number of rounds to be played.
        nums (list): A list of integers representing numbers for each round.

    Returns:
        str or None: The name of the winner or None if there is no winner.

    """
    def sieve(n):
        """
        Implements the Sieve of Eratosthenes algorithm.

        Parameters:
        n (int): The upper limit of the range to find prime numbers.

        Returns:
        list: A boolean list where each index represents a number from 0 to n,
        and the value at each index indicates whether number is prime or not.
        """

        primes = [True for _ in range(n+1)]
        p = 2
        while p * p <= n:
            if primes[p] is True:
                for i in range(p * p, n+1, p):
                    primes[i] = False
                p += 1
        return primes

    max_num = max(nums)
    primes = sieve(max_num)
    maria_wins = ben_wins = 0

    for num in nums:
        prime_count = sum(1 for i in range(2, num+1) if primes[i])
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
