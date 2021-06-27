# A Pythagorean triplet is a set of three natural numbers,
#  a < b < c, for which, a^2 + b^2 = c^2
# 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


# Found this online for finding pythagorean triples
# When m and n are any two positive integers (m > n):
#
#    a = m^2 − n^2
#    b = 2mn
#    c = m^2 + n^2


# Turning into code what is written above, as a function. returns as a list
def make_triple(m, n):
   a = (m * m) - (n * n)
   b = 2 * m * n
   c = (m * m) + (n * n)
   triple = [a, b, c]
   triple.sort()
   return triple

# test to see if all the elements of the triple are equal to a majic number (which will be 100 for us)
def majic_triple_test(testTriple, majicNum):
    total = 0
    for side in testTriple:
        total += side 
    if total == majicNum:
        return True
    else:
        return False


i = 1
j = 2

# nested loop, J must be bigger than I
while j < 1000:

    # While i is less than j, make a triple
    while i < j:
        magicTriple = make_triple(j, i)
        
        # then check to see if its majic, if so, find the product, and print
        if majic_triple_test(magicTriple, 1000):

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