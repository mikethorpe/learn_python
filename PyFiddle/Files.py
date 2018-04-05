

# read mode
# file = open("file.txt")
# file = open("file.txt", "r")

# write mode
# file = open("file.txt", "w")

# binary write mode - image and sound files (non text based)
# file = open("file.txt", "wb")

# binary read mode
# file = open("file.txt", "rb")

# append mode
# file = open("file.txt", "a")

# close the file when you are done
# file.close()

file = open("file.txt")

# Read the first byte of the file
# Note - 1 byte is 1 character
first_1_bytes_of_contents = file.read(1)
print(first_1_bytes_of_contents)

# Read the rest of the file
file_contents = file.read()
print(file_contents)

# have come to the end of the file on the read above so the
# below will return an empty string
file_contents_on_second_read = file.read()
print(file_contents_on_second_read)


# Get a list of lines in the file as strings
file = open("file.txt")
listOfLinesAsStrings = file.readlines()
print(listOfLinesAsStrings)
file.close()

# Read the lines from the file one by one
file = open("file.txt")
listOfLines = [ ]

for line in file:
    listOfLines.append(line)

file.close()

for line in listOfLines:
    print(line)

print(listOfLinesAsStrings)


# Writing files - creates a file of this name if
# it does not exist. the process of opening it in
# write mode deletes all content if it does exist.
file = open("file.txt", "w")
file.write("line for the file")

# file.write() returns the number of bytes written
# to the file if successful
numberOfBytesWritten = file.write("another line for the file")
file.close()

print("number of bytes written to the file :" + str(numberOfBytesWritten))

# Good practise to always close with a finally block so that whatever happens
# the file isn't left open and you can regain access

try:
    file = open("file.txt", "w")
    file.write("someline")

finally:
    file.close()


# alternatively do the following:
# with creates temp variable called f which is disposed of at the end of
# the block
with open("file.txt") as f:
   print(f.read())
