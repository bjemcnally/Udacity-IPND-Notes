# Equality Comparisons Quiz

# Making Decisions!

print 2 < 3 # output is True
print 21 < 3 # output is False 
print 7 * 3 < 21 # False
print 7 * 3 != 21 # False

print 7 * 3 == 21 # True

# Why is the equality comparison done using == instead of =?

# MY ANSWER

# because = means assignment!
# CORRECT!


# If Statements Quiz

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

# MY ANSWER

def bigger(x, y):
  if x > y:
    return x
  else: # haven't technically learned this yet!
    return y

# THIS WORKED

print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3

# Video answer:

def bigger(a, b):
  if a > b:
    return a
  return b

# If Friend Quiz

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

# MY ANSWER

def is_friend(s):
  if s[0] == 'D':
    return True
  else:
    return False

# This worked!


print is_friend('Diane')
#>>> True

print is_friend('Fred')
#>>> False

# Video Answer

def is_friend(name): # remember to make your parameters descriptive!
    if name[0] == 'D':
        return True
    else:
        return False

# the answer could also be much shorter:

def is_friend(name):
    return name[0] == 'D'

# More Friends Quiz

# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

# MY ANSWER

def is_friend(name):
    if name[0] == 'D':
        return True
    if name[0] == 'N':
        return True
    else:
        return False

# This worked!



print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False

# Video Answer

def is_friend(name):
    if name[0] == 'D':
        return True
    if name[0] == 'N':
        return True
    return False # this answer is a bit shorter than mine!

# OR...

def is_friend(name):
    if name[0] == 'D':
        return True
    else:
        if name[0] == 'N':
            return True
        else:
            return False # this answer has more code, but shows structure better

# better yet, include OR operator:

def is_friend(name):
    return name[0] == 'D' or name[0] == 'N'

print is_friend('Doug')
print is_friend('Nicole')

# Biggest Quiz

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

# MY ANSWER, we haven't used AND operator yet, but I'm going to cheat...

def biggest(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    else:
        return c

# This worked... how would I do it without and, just or?

def biggest(a, b, c):
    if a >= b:
      if  a >= c:
        return a
    if b >= c:
      if b >= a:
        return b
    else: 
        return c

# without equals signs, biggest(2, 2, 1) does not return the correct value!
# but I got the right answer eventually without looking!


print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9

# Video Answer

def biggest(a, b, c):
    if a > b:
        if a > c: # a is the biggest
            return a
        else:
            return c # c is the biggest
    else: # if a < b
        if b > c:
            return b # b is biggest
        else: return c

# an alternative would be to use bigger TWICE!

def biggest(a, b, c):
    return bigger(bigger(a,b),c)

# OR use max() operator:

return max(a,b,c)

# at this point, we have learned enough to define every built in function in Python!
# and every possible computer program!!! everything that computed mechanically can
# be coded using the things we've seen so far: functions, arithmetic, comparisons, and if statements