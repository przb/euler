# The sum of the squares of the first
# ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first
# ten natural numbers is,
# (1+2+...+10)^2 = 55^2 = 3025
#
# Hence the difference between the
# sum of the squares of the first
# ten natural numbers and the square
# of the sum is
# 3025 - 385 = 2640
#
# Find the difference between the sum
# of the squares of the first one hundred
# natural numbers and the square of the sum.


# Initialize all variables
sumOfSquares = 0
sum = 0
i = 0
targetNum = 100


while i <= targetNum:

    # square i, then add it to the sum of the squares
    sumOfSquares = (i * i) + sumOfSquares

    # take the sume of the numbers less than or equal to targetNum
    sum = sum + i

    i += 1

# Square the sum of all numbers less than or equal to 100
squareOfSum = sum * sum

# Sumbtrack the square of the sum from the sum of the squares
difference = squareOfSum - sumOfSquares

print(difference)
