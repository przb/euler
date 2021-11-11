import math


def is_palindrome(number):

    number = str(number)
    index = 0
    lastIndex = len(number) - 1
    if not (number[index] == number[lastIndex - index]):
        return False
    else:
        palindromeStatus = True

        while (lastIndex - index > 1):
            if not (number[index] == number[lastIndex - index]):
                palindromeStatus = False
                return palindromeStatus
            else:
                index += 1

        return palindromeStatus


def decrement_multiply(static_num, index_num):
    while index_num > 1:
        product = static_num * index_num
        if is_palindrome(product):
            return product
        index_num -= 1
    return 0


def find_all_prime_factors(mainNum):

    # The target variable is first initialized to the number that is passed to the method
    target = mainNum

    # The index is initialized to two becuase the index will be multiplied later,
    #  and 1 is not necessary
    i = 2

    # Initialize an empty list to store the prime factors (not just the unique ones)
    primeFactors = []

    while (i <= target):

        # if the target is divisible by the index, the index will be added to the
        # prime factors list. The target will also be divided by the index so that
        # we can get the rest of the prime factors.
        #
        # Its like if 20 is divisible by 5, then add 5 to the list, then make the new
        # target = 20/5 (which is 4), and find the prime factor of 4
        if target % i == 0:
            primeFactors.append(i)
            target /= i

        # If the index equals the target, that means the index has reached the last
        # prime factor and the index will be added to the primeFactors list.
        #
        # Useful for prime numbers. If the target were 7, it would increment until
        # it reached 7. Then it would add 7 to the list
        elif i == target:
            primeFactors.append(target)

        # If the index is not divisible, and it is not the last prime factor,
        # increment the list
        else:
            i += 1

    return primeFactors


def find_primes_less_than(maxPrime):
    primes = [2, 3]
    i = 3
    primeCheck = 5
    while primeCheck < maxPrime:

        while i < primeCheck:
            if primeCheck % i == 0:
                break
            elif i >= math.sqrt(primeCheck):
                primes.append(primeCheck)
                break
            else:
                i += 1
        primeCheck += 2
        i = 3

    return primes


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
