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
