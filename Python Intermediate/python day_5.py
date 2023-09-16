#opening the file
file = open("data.txt","r")

lines = 0


#iterate the lines
for line in file:
    lines += 1

#closing the file
file.close()

#print the number of lines in data.txt

print(f"total line in the file: {lines}")
