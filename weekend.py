# Weekend Quiz

# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    # MY ANSWER
    if day == 'Saturday' or day == 'Sunday':
        return True
    else:
        return False

# THIS WORKED
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False

# Blastoff Quiz

# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

# MY ANSWER

def countdown(n):
    x = n
    while x >= 1:
        print x
        x -= 1
    if x == 0:
        print 'Blastoff!'

# THIS WORKED!
s
countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!

# Video ANSWER

def countdown(n):
    while n > 0:
        print n
        n = n - 1
    print "Blastoff!" # this is essentially an else statement

# Median Quiz

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

# MY ANSWER    

def median(a, b, c):
    if a > b:
        if c < a and c > b:
            return c
        if c > a:
            return a
    if c > a and c < b:
        return c
    if c > b:
        return b # THIS DID NOT WORK FOR 7, 8, 7

def median(a, b, c):
    if a >= b:
        if c <= a and c >= b:
            return c
        if c >= a:
            return a
    if c >= a and c <= b:
        return c
    if c >= b:
        return b # THIS ALMOST WORKED

def median(a,b,c):
    if a >= b:
        if c <= a and c >= b:
            return c
        if c >= a:
            return a
    if c >= a and c <= b:
        return c
    if c >= b:
        return b
    else:
        return a # THIS FAILED ON 3, 2, 1

def median(a,b,c):
    if a >= b:
        if c <= a and c >= b:
            return c
        if c >= a:
            return a
        return b
    if c >= a and c <= b:
        return c
    if c >= b:
        return b
    else:
        return a # THIS FINALLY WORKED


print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7

# Video ANSWER

def median(a,b,c):
    big = biggest(a,b,c) # eliminates one number as median
    if big == a:
        return bigger(b,c)
    if big == b:
        return bigger(a,c)
    else:
        return bigger(a,b)

# Random Nouns Quiz

# Write code for the function random_noun, which takes in no inputs but outputs 
# one of two nouns randomly. Use the randint function to generate a number 
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1. 
# Feel free to experiment with different nouns, but for submission purposes return 
# the string "sofa" if the number is 0, else return "llama".

from random import randint

def random_noun():
    # MY ANSWER
    num = randint(0,1)
    if num == 0:
        return 'sofa'
    return 'llama'

# This worked!

# Video ANSWER

def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

# Random Verbs Quiz

# Write code for the function random_verb, which takes in no inputs but outputs 
# one of two verbs randomly. Use the randint function to generate a number from 0-1 
# and return a verb depending on whether the number is equal 0 or 1. Feel free to 
# experiment with different verbs, but for submission purposes return the string "run"
# if the number is 0, else return "kayak".

from random import randint

def random_verb():
    # MY ANSWER
    random = randint(0,1)
    if random == 0:
        return "run"
    return "kayak"

print random_verb() 

# THIS WORKED! and is essentially the same as the video ANSWER




     
