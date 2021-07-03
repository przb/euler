# Open and read the file
file = open("p11_number_grid.txt", "r")
line = file.readlines()
file.close()

# initialize empty variables
i = 0
j = 0
abs = 1 # absolute index, total number of index
data = []


# Parse the text file to a list, each row is a list in the list
for digits in line:
    row = digits.strip().split(" ")
    data.append(row)
# print(data)



while i < len(data):
    while j < len(data[i]):
        print(f"{abs}:{data[i][j]}")
        j += 1
        abs += 1
    i += 1
    j = 0
     
# for a in data:
#     for b in a:
#         print(b)
