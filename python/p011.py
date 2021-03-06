# In the 20×20 grid below, four numbers along a diagonal 
# line have been marked in red.
# 
# (text file)
# 
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# 
# What is the greatest product of four adjacent 
# numbers in the same direction (up, down, left, 
# right, or diagonally) in the 20×20 grid?
# 


# Open and read the file
file = open("p11_number_grid.txt", "r")
rawFileData = file.readlines()
file.close()

# make some temp lists for data
fileData = []
tempList = []

# proccess the data to a two dimensional list and convert to ints
for line in rawFileData:
    line = line.strip().split(" ")
    for digit in line:
        #print(digit)
        tempList.append(int(digit))
    line = tempList
    fileData.append(tempList)
    tempList = []


def horz_mult(row, ADJACENT_NUMS):
    i = 0
    maxProduct = 1
    while i <= len(row) - ADJACENT_NUMS:
        tempProduct = 1
        multipliers = row[i:i + ADJACENT_NUMS]
        for multiplier in multipliers:
            tempProduct *= multiplier
        if maxProduct < tempProduct:
            maxProduct = tempProduct
        i += 1
    return maxProduct

def vert_mult(twoDList, row, ADJACENT_NUMS):
    maxProduct = 1
    for n in range(row, len(twoDList)):
        currentProduct = 1
        for m in range(row, row + ADJACENT_NUMS):
            currentProduct *= twoDList[m][n]
            print(currentProduct)
        if currentProduct > maxProduct:
            maxProduct = currentProduct
        currentProduct = 1
    return maxProduct

def diag_mult(twoDList, row, ADJACENT_NUMS):
    for oneDList in range(0, len(twoDList)):
        for m in range(0, len(twoDList)):
            print(m)
        
            

i = 0
j = 0

ADJACENT_NUMS = 4
# for fileRow in fileData:
#    print(horz_mult(fileRow, ADJACENT_NUMS))
print(diag_mult(fileData, 0, ADJACENT_NUMS))