# While Loops Quiz

# first an example

i = 0
while i < 10:
    print i
    i = i + 1

# loops through until test expressoin (i > 10) is no longer True
# the new value of i is now 10!

print i

# Quiz question: What does this program do?

i = 0
while i != 10:
    i = i + 1
    print i

# My answer: Print out numbers from 1 to 9 (I think that once i = 10, it will stop the loop, also, unlike the loop above, this won't print 0 because print comes after i = i + 1)

# WRONG! It will also print 10...

# Video Answer:

# Because we print 10 before we perform the while test!

# While Loops 2 Quiz

# What does this program do?

# i = 1
# while i != 10:
#     i = i + 2
#     print i

# My answer: i will never = 10! I think this will run forever because the test expression will never be False

# CORRECT! this is an infinite loop

# Print Numbers Quiz

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

# hint: will require function, variable, and while loop

# MY ANSWER:

def print_numbers(x):
    y = 1
    while y <= x:
        print y
        y = y + 1

# Took a couple of tries, but this worked!

print_numbers(3)
#>>> 1
#>>> 2
#>>> 3

# Video Answer is essentially identical to mine!

# Second video answer:

def print_numbers2(n):
    j = 0
    while j < n:
        j = j + 1
        print j

print_numbers2(4)


# Break Statements

def print_numbers3(n):
    k = 1
    while True:
        if k > n:
            break
        print k
        k = k + 1

# This will have the same outcome as the print_numbers2 above (print_numbers2 is better)


