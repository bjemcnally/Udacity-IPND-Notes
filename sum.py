# Sum Procedure (Function Quiz)
# What does the sum function do?

def sum(a, b):
    a = a + b

# My answer:
# Takes two numbers as inputs and changes the value of the first (a) to be the sume of the two numbers

# I was wrong, it does NOTHING! sum() doesn't return the new value of a

# without a return, functions don't produce any output

print sum(1, 1) # returns None, no value!

def sum(a, b):
    print "enter sum!"
    print "a is", a
    a = a + b
    print "a is", a

print sum(2, 123) # code works, but function needs a return statement!

def sum(a, b):
  a = a + b
  return a

print sum(2, 123)

# if we define variables like this:

a = 2
b = 123
print sum(a, b)
print a # this still refers to 2, because function did not change the value of the variable (a)

# Sum Function with a Return Statement
# same question as before, now with a return statement (i.e. lines 24-26)

# NOW: all of the above? (NOPE)

# Video answer: takes numbers as inputs and outputs their sum and/or takes strings and outputs their concatenation:

s = 'Hello '
t = 'Joy!'
print sum(s, t)
print s # still does not change the value of s itself!