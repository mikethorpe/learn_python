# appends elements to a list
nums = [1, 2, 3]
nums.append(4)
print(nums)

# get the length of a list
nums = [1, 3, 5, 2, 4]
print(len(nums)) #  could use list.count(obj) instead

# or you could use this for a string
print(len("123"))

nums.insert(1, "inserted string")
print(nums)

# gets first index of element if it exists, returns value error if not
int_indexOfString = nums.index("inserted string")
print(int_indexOfString)

# There are a few more useful functions and methods for lists. 
# max(list): Returns the list item with the maximum value
# min(list): Returns the list item with minimum value
# list.count(obj): Returns a count of how many times an item occurs in a list
# list.remove(obj): Removes an object from a list
# list.reverse(): Reverses objects in a list


# range = used to generate a list of numbers in a range
list_int_range = list(range(5))
print list_int_range

list_int_range = list(range(2,5))
print list_int_range

# third arguement defines increment of numbers
numbers = list(range(5, 20, 2))
print(numbers)

# foreach loops
string_someStrings = ["one", "two", "three", "four"]
for string in string_someStrings:
    print(string)

#for loop standard
for i in range(5):
	print("hello!")
