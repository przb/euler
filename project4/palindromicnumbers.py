# A palindromic number reads the same both ways. 
# The largest palindrome made from the product 
# of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from 
# the product of two 3-digit numbers.


def is_palindrome(number):
    
    number = str(number)
    index = 0
    lastIndex = len(number) - 1
    
    if not (number[index] == number[lastIndex - index]):
        return False

    while (lastIndex - index > 1):
        if not (number[index] == number[lastIndex - index]):
            return False
        else:
            index += 1
    
    return True

bigFactor = 999
indexFactor = 999
product = 0
finalProduct = 0
while product != 1 :
    if bigFactor == indexFactor and (not is_palindrome(product)):
        product = bigFactor * indexFactor
        indexFactor -= 1
    elif bigFactor > indexFactor and (not is_palindrome(product)):
        product = bigFactor * indexFactor
        while indexFactor >= 1 and (not is_palindrome(product)):
            product = bigFactor * indexFactor
            indexFactor -= 1
        bigFactor -= 1
    else:
        print("error")

    if product > finalProduct: 
        finalProduct = product
print(finalProduct)