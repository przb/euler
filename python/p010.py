# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

import custom_math_functions

total = 0

primes = custom_math_functions.find_primes_less_than(2000000)

for number in primes:
    total += number
print(total)