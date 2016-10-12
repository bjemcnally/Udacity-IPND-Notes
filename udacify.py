# Udacify Quiz

# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'

# MY ANSWER

def udacify(input):
  return 'U' + input

# this worked
  
# Remove the hash, #, from infront of print to test your code.

print udacify('dacians')
#>>> Udacians

print udacify('turn')
#>>> Uturn

print udacify('boat')
#>>> Uboat

# Video answer:

def udacify(s):
  return 'U' + s


# Print vs Return Quiz

# Which of the following will print?

def double1(x):
  return 2 * x # this won't print

def double2(x):
  print 2 * x # this will print

def double3(x):
  return 2 * x
  print 2 * x # this will print (APPARENTLY NOT, BECAUSE RETURN STATEMENT
  # IS BEFORE PRINT STATEMENT, THE PRINT STATEMENT WILL NEVER BE EXECUTED!!)

def double4(x):
  print 2 * x
  return 2 * x # this will also print

# Video answer