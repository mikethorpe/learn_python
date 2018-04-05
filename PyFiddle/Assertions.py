'''
M.A. Thorpe 2018
Fiddle about assertions
'''

# checks that the statement is true and returns
# an exception if it is not - this can be used
# in the first line of a function to check validity
# of its arguments. It can also be used after a
# function has been called to check validity of 
# outputs
assert 2+2 == 4
assert (2+1 == 4), "Wow - that sum was not right!"
