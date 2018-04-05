''' M. A. Thorpe 2018
Learning python
'''

# Print Your code here
print('Hello in console window')
print('print some string')
stringHello = "hello"
print(stringHello)
int_myFirstInt = 42

print(int_myFirstInt)

# We can multiply strings
print("Multiply strings example")
print(stringHello * 3)


# If statement example
bool_myBool = True
bool_mySecondBool = False

if bool_myBool == True:
    print("first statement executed")
else:
    print("Second statement executed")
    
# If statements can be nested
if bool_myBool == True:
	if bool_mySecondBool == True:
		print("Nested statement executed")

# Note: elif: = else if()

# Boolean operators:

if bool_myBool and bool_mySecondBool == True:
    print("boolean and is true")
    
if bool_myBool or bool_mySecondBool == True:
    print("boolean or is true")
 
# Prints the line if the bools are different
if not bool_myBool == bool_mySecondBool:
    print("boolean not is true")
    

# while loops

int_i = 0
while int_i < 5:
    
    # example continue statement
    if int_i == 2:
        continue
    print("This is a while loop")
    int_i += 1
    
    #example break statement
    if int_i == 3:
        print("loop broken")
        break
    
    
# list example - are crazy can contain multiple types and nested lists
things = ["string", 0, [1, 2, number], 4.56]

nums = [1, 2, 3]
print(nums + [4, 5, 6]) # adds three extra elements (similar to strings)
print(nums * 3) # adds 6 extra elements of the same value (similar to strings)

# check if an item is in a list
if 1 in nums:
    print("1 is in nums")
    
# check if an item not in a list
if not 12 in nums:
    print("1 is in nums")
