# The four adjacent digits in the 1000-digit number 
# that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# 
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
# 
# Find the thirteen adjacent digits in the 1000-digit
#  number that have the greatest product. What is the 
#  value of this product?
# 

# Retrieve the larger number from the file
file = open('/home/przb/Workspaces/euler/p8_big_number.txt', 'r')
BIG_NUMBER = file.read().strip().replace("\n", "")
file.close()

# Declare some variables 
adjacency = 13          # how many adjacent numbers to use
i = 0                   # index for offset of numbers that were adjacent
largestProduct = 1      # Final product to store the largest product
largestThirteen = 0     # The number that gives the numbers that equal the largestProduct
tempProduct = 1         # Temporary to store the product of some numbers


while i <= len(BIG_NUMBER) - adjacency:

    # The adjacent numbers start with 0:13, then 1:14, then 2:15 and so on
    tempDigits = BIG_NUMBER[i:i + adjacency]


    for digit in tempDigits:

        # find the temporary product
        tempProduct *= int(digit)

        # if the largest product is less than the temp product make, make the largest product 
        # equal to the temp, and set the largest 13 to the current thirteen
        if largestProduct < tempProduct:


            largestProduct = tempProduct


            largestThirteen = tempDigits

    # reset the product back to 1 and increment the index
    tempProduct = 1
    i += 1

# at the end, print the results
print(f"Largest Thirteen adjacencies: {largestThirteen}")
print(f"Largest Product: {largestProduct}")