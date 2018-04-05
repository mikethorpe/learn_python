''' 
M. A. Thorpe 2018
Learning about exceptions in Python
'''

# Common exceptions:
# ImportError: an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly; 
# TypeError: a function is called on a value of an inappropriate type;
# ValueError: a function is called on a value of the correct type, but with an # inappropriate value.

# Catch exceptions as below
try:
    value = 5/0
except ZeroDivisionError:
    print("Well that didn't work, try dividing by a sensible number...like NOT ZERO!")

# catch mulitple error types
except (ValueError, TypeError):
    print("Some other error")

# catch everything
except:
    print("Catch everything")

# finally always executes
finally:
    	print("Always print this")
 		# we can deliberately raise an exception - we must specify its type - we can give extra info in the brackets
        raise ValueError("This is the wrong value")
