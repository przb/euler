# A palindromic number reads the same both ways. 
# The largest palindrome made from the product 
# of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from 
# the product of two 3-digit numbers.

import custom_math_functions

bigFactor = 999
indexFactor = 999
largestPalindrome = 0
while bigFactor > 1:
    biggestTestNum = custom_math_functions.decrement_multiply(bigFactor, indexFactor)
    if largestPalindrome < biggestTestNum:
        largestPalindrome = biggestTestNum
    bigFactor -= 1

print(largestPalindrome)