# By listing the first six prime numbers:
#  2, 3, 5, 7, 11, and 13, we can see that 
#  the 6th prime is 13.
# 
# What is the 10 001st prime number?

import custom_math_functions

#initialize two indexes started with relevant prime numbers
i = 3
j = 2

#initialize a list with 2 to start
primeNumbers = [2]


while len(primeNumbers) <= 10000:

    while i > j:

        # if the larger index is divisible by the smaller index, break the loop. Its not prime
        if i % j == 0:
            break

        #if the smaller index is larger than half of the greater index, and it is still not
        # divisible by each other, i will consider it prime, and reset the smaller index
        elif j > i/2:
            primeNumbers.append(i)
            j = 3
            break

        # if none of those, increment the smaller index
        else:
            j += 1

    #increment the larger index by two, to keep it odd
    i += 2

    # reset the smaller index to 3
    j = 3

# print the last prime numer in the list
print(primeNumbers[-1])