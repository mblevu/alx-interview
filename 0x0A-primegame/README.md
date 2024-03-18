
# Prime game


1. Create a function `sieve` that generates all prime numbers up to a given number using the Sieve of Eratosthenes algorithm.
2. In the `isWinner` function, find the maximum number in the `nums` array.
3. Generate all prime numbers up to the maximum number using the `sieve` function.
4. Initialize counters for Maria and Ben's wins to 0.
5. For each round, simulate the game:
   1. Initialize a counter for the number of primes in the current round.
   2. For each prime number up to the number for the current round, increment the counter.
   3. If the counter is odd, Maria wins the round, so increment Maria's counter. Otherwise, Ben wins, so increment Ben's counter.
6. If Maria's counter is greater than Ben's, return "Maria". If Ben's counter is greater, return "Ben". If they are equal, return None.