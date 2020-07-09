"""
Title: problem1.py
Problem: If we list all the natural numbers below 10 that are multiples
            of 3 or 5 we get: 3, 5, 6, 9. If we sum these we get 23.
            Find the sum of all the multiples of 3 or 5 below 1000.
Notes:
"""
import numpy as np


# Initialize the sum
multSum = 0

# Loop over the multiples of 3. Only need to loop until max multiple
for i in range(3, 1000, 3):
    multSum += i

# Now loop over the multiples of 5. Do the same thing, but we need to
# avoid double counting those multiples that are common to 3 and 5
for i in range(5, 1000, 5):
    if i % 3 != 0:
        multSum += i

print("Sum of multiples: {}".format(multSum))
