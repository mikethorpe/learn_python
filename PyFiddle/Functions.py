''' M.A.Thorpe 2018
This is a fiddle about functions
'''

# This is how we define a function
def add_two_numbers(x, y):
	return x + y

# This is how we call the function

i = 1
j = 2

result = add_two_numbers(i, j)
print(result)

# We can assign a function to a variable

adding_function = add_two_numbers

new_result = adding_function(2,3)
print(new_result)

# We can also pass functions to functions

def function_result_plus_number(func, number):
    return
