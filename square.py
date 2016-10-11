# Square Quiz

# Define a procedure, square, that takes one number 
# as its input, and returns the square of that 
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

def sum(a,b):
    c = a + b
    return c

def square(n):
    return n * n

# MY ANSWER WORKED


# To test your procedure, uncomment the print 
# statement below, by removing the hash mark (#) 
# at the beginning of the line.

# Do not remove the # from in front of the line 
# with the arrows (>>>). Lines which begin like 
# this (#>>>) are included to show the results
# you should see when run your procedure.

print square(5)
#>>> 25

# Video answer is exactly the same as mine

x = 37
print square(x)
print square(square(x)) # this is called procedure composition!

# Sum of Three Quiz

# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.

def sum(a,b):
    return a + b

# MY ANSWER:

def sum3(d, e, f): # don't forget the colon!
  return d + e + f

# This worked!


print sum3(1,2,3)
#>>> 6

print sum3(93,53,70)
#>>> 216

# Video Answer:

def sum3(a, b, c): # generally best to name your inputs more descriptively!!!
  return a + b + c

# Abbaize Quiz

# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.

# MY ANSWER:
def abbaize(string1, string2):
  return string1 + (string2 * 2) + string1
# THIS WORKED


print abbaize('a','b')
#>>> 'abba'

print abbaize('dog','cat')
#>>> 'dogcatcatdog'

# Video answer:

def abbaize(a, b):
  return a + b + b + a