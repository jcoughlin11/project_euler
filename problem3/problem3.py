"""
Problem: The prime factors of 13195 are: 5, 7, 13, and 29. What is
            the largest prime factor of 600851475143?
Notes: *https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
        * Upper limit optimization:

        Let N = 10, and we're doing the sieve:

        1 2 3 4 5 6 7 8 9 10

        We can start at n = 2, looping until n > N and incrementing n
        by n:

        [2] 3 {4} 5 {6} 7 {8} 9 {10}

        We now go to the next non-curly braced item, which is 3. So,
        n = 3 and we loop until n > N and incrementing n by n:

        [2] [3] {4} 5 {{6}} 7 {8} {9} {10}

        The double braces means that number was flagged by both 2 and 3.
        Now n = 5:

        [2] [3] {4} [5] {{6}} 7 {8} {9} {{10}}

        Now n = 7:

        [2] [3] {4} [5] {{6}} [7] {8} {9} {{10}}

        All of the [] numbers are primes. Note that for every n after
        n = 2, when looking at the multiples of that prime, we could have
        started at n^2 instead of 2n because all multiples up to (but not
        including) n^2 have already been flagged as being the multiple
        of a previous prime. As an example, when looking at multiples of
        3, 6 has already been crossed off as not prime because it's also
        a multiple of 2. As such, the first multiple of 3 in the list
        not already crossed off is 9.

        The multiples of n = 2 are: 2*2, 3*2, 4*2, 5*2, ... and each of
        these gets crossed off the list. The multiples of n = 3 are:
        2*3, 3*3, ... and 2*3 == 3*2, which shows up in the multiples of
        two list. Thus, we start at the next multiple, which, is always
        going to be n^2 (since all other combinations of n and multiple
        m will have already occurred). For 5: 2*5 (the only multiple of
        5 in range of N) has already happened.
"""
import math


# Number to find largest prime factor of
N = 600851475143
# N = 13195
# Largest prime factor
lpf = None
# Max value to check.
upperLim = int(math.sqrt(N)) + 1


# Start by dividing N by 2, the first prime number
while N % 2 == 0:
    N /= 2
    lpf = 2
# Now N must be odd, so we can start the search at 3 and go by 2, since
# there will be no more even primes
for i in range(3, upperLim, 2):
    if N % i == 0:
        N /= i
        lpf = i
print(lpf)
