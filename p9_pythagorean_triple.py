# A Pythagorean triplet is a set of three natural numbers,
#  a < b < c, for which, a^2 + b^2 = c^2
# 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import custom_math_functions

i = 1
j = 2

# nested loop, J must be bigger than I
while j < 1000:

    # While i is less than j, make a triple
    while i < j:
        magicTriple = custom_math_functions.make_triple(j, i)
        
        # then check to see if its majic, if so, find the product, and print
        if custom_math_functions.majic_triple_test(magicTriple, 1000):

            product = 1

            for triplet in magicTriple:
                product *= triplet

            print(magicTriple, product)

        # increment i, while I is less than J
        i += 1

    # Increment J until it is 1000
    j += 1

    #reset I to 1
    i = 1