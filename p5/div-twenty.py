# 2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is 
# evenly divisible by all of the numbers from 1 to 20?

# Its hard to explain in typing what how this mathematically works, but it does work

import prime_factors

# Set the number in the goal
divByAllNum = 20

# Initialize the total and the index (which is set to 2 because it is later multplied)
total = 1
i = 2

# Initialize an empty list to store all the factors
allFactors = []


while  i <= divByAllNum:

    # Calls upon my other method that finds all the prime factors of i
        
    primeFactors = prime_factors.find_all_prime_factors(i)
    i += 1

    # Adds a prime factor to allFactors, if there are more of said prime factor in
    # the number previous list

    # basically the prime factors of 6 are 2 and 3
    # the prime factors of 9 are 3 and 3
    # so we need to make sure there are at least two 3s in the list
    for factor in primeFactors:
        if allFactors.count(factor) < primeFactors.count(factor):
            allFactors.append(factor)
    
# This part finds the answer. The product of all the prime factors of
# all numbers <= 20 is the first number that is evenly divisible by 
# all numbers <= 20
for uniqishFactor in allFactors:
    total = total * uniqishFactor 

print(allFactors)
print(total)