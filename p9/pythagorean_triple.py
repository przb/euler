# A Pythagorean triplet is a set of three natural numbers,
#  a < b < c, for which, a^2 + b^2 = c^2
# 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math


def is_triple(ayy, bee):
    cSquared = math.pow(ayy, 2) + math.pow(bee, 2)
    if math.pow(int(math.sqrt(cSquared)), 2) == cSquared:
        return True
    else: 
        return False

# p^2 + q^2 = r^2
# p is always odd
# q = (p^2 - 1)/2
# 
# 
# 
# 

triples = []
tempList = []
limit = 100
p = 1
a = 1
b = 2
c = 3

while p < limit:
    q = ((p * p) - 1) / 2
    if math.pow(int(q), 2) == math.pow(q, 2):
        print(f"{p}^2 + {int(q)}^2 = r ")
    p += 2
