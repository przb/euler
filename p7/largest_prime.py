# By listing the first six prime numbers:
#  2, 3, 5, 7, 11, and 13, we can see that 
#  the 6th prime is 13.
# 
# What is the 10 001st prime number?


i = 3
j = 2
primeNumbers = [2]
while len(primeNumbers) <= 10000:
    while i > j:
        if i % j == 0:
            # print("1")
            break
        elif j > i/2:
            primeNumbers.append(i)
            j = 3
            # print("2") 
            break
        else:
            j += 1
            # print("3")
    i += 2
    j = 3
print(primeNumbers[-1])