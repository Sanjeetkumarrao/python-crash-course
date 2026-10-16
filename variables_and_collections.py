# Python has a print function
print("I'm Python. Nice to meet you!")

# by default the orint function also prints prints  out a newline at the end.
print("Hello, World", end="!") # => Hello, World!

# simple way to get input data from console
imput_string_var = input("Enter some dT: ") # Returns the dT as a string

# there are no declarations, only assignments.
# Convention in naming variables in snake_case style
some_var = 5 
some_var # => 5

# Accessing a previously unassigned variables is an exception.
# See control flow to learn more about axception handling.
some_unknown_var # Raises a NameError

# if can be used as an expression
# Equivalent of C's '?:' ternary operator
"yay!" if 0 > 1 else "nay!" # "nay!"

# lists store sequences 
li = []
# Yout can start with a prefilled list
other_li = [4,5,6]

# add stuff to the end of a list with sppend
li.append(1)    # li is now [1]
li.append(2)    # li is now [1,2]
li.append(4)    # li is now [1,2,4].
li.append(3)    # li is now [1,2,4,3]

# remove from the end with pop
li.pop()  # => 3 and li is now [1,2,4]