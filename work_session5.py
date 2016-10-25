# Exploring List Properties Quiz 2

# What is the difference between these two pieces of code?
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

def proc(mylist):
    mylist = mylist + [6, 7]

def proc2(mylist):
    mylist.append(6)
    mylist.append(7)

# Can you explain the results given by the print statements below?

print "demonstrating proc"
print list1
proc(list1)
print list1
print
print "demonstrating proc2"
print list2
proc2(list2)
print list2

# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1,2,3,4,5]
list3 += [6, 7]

# Does this behave like list1 = list1 + [6,7] or list2.append([6,7])? Write a
# procedure, proc3 similar to proc and proc2, but for +=. 

# My answer

def proc3(my_list, new):
    my_list += new
    return  my_list
    
list4 = [1,2,3,4,5]

print "Testing proc3"    
print proc3(list4, [6])

# this worked!

# While Loop 1 Quiz

# Let's learn a little bit of Data Analysis and how we can use
# loops and lists to create, aggregate, and summarize data

# For the part 1, we'll learn a basic way of creating data using
# Python's random number generator.

# To create a random integer from 0 to 10, we first import the 
# "random" module

import random

# We then print a random integer using the random.randint(start, end) function
print "Random number generated: " + str(random.randint(0,10))

# Remember that if we want to concatenate a string and a number, we need to convert the 
# integer into a string using the str() function

# We now want to create a list filled with random numbers. The list should be 
# of length 20

random_list = []
list_length = 20

# Write code here and use a while loop to populate this list of random integers. A crucial
# function that will help you is to use the append() method to add elements to a list.

# MY ANSWER

def list_of_random(length):
    start = 0
    while start < length:
        new = random.randint(0,10)
        random_list.append(new)
        start += 1
    return random_list

list_of_random(list_length)

# this worked!

# When we print this list, we should get a list of random integers such as:
# [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
print random_list

# Provided answer 1:

import random

random_list = []
list_length = 20

while len(random_list) < list_length:
   random_list.append(random.randint(0,10))

# Provided answer 2:

random_list = []
list_length = 20
count = 0

while count < list_length:
   random_list.append(random.randint(0,10))
   count += 1

# While Loop 2 Quiz

# Know we want to ask our self the question:
# How many occurrences of the number 9 appear in our randomly made list?
# For example if we have a list: [2,8,9,9,4,5,9], we want to figure out
# how to go loop through the list and count how many occurrences of the
# number 9. In this example, the number 9 occurs 3 times in the example
# list

import random

# 1. Create random list of integers using while loop
random_list1 = []
list_length = 20

while len(random_list1) < list_length:
  random_list1.append(random.randint(0,10))
    
# Write code here to loop through the list and count all occurrences
# of the number 9. If statements and While loops will help you solve
# this problem.

# MY ANSWER

def count9s(a_list):
    count_1 = 0
    for each in a_list:
        if each == 9:
            count_1 += 1
    return count_1

# this worked


# Test if our While loop we wrote works, we should manually count
# how many times the number 9 is present in the list.
print random_list1
print count9s(random_list1)

# Provided answer:

import random

random_list = []
list_length = 20

while len(random_list) < list_length:
   random_list.append(random.randint(0,10)) # this builds the list

index = 0
count = 0

while index < len(random_list):
  if random_list[index] == 9:
    count = count + 1
  index = index + 1 # index is the length of the list

